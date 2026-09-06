"""Machine lifecycle wait helpers.

These helpers sit on top of the generated SDK and implement the common
"create a machine, then wait until it is usable" workflow that official
examples currently hand-roll with sleep + retrieve loops.

Example::

    from dedalus_sdk import Dedalus
    from dedalus_sdk.lib.machine_wait import create_and_wait, wait_until_running

    client = Dedalus()
    machine = create_and_wait(
        client,
        memory_mib=2048,
        storage_gib=10,
        vcpu=1,
        on_status=lambda m: print(m.status.phase),
    )
"""

from __future__ import annotations

import time
from typing import Any, Callable, Iterable, Optional, Sequence, Union

from dedalus_sdk import Dedalus
from dedalus_sdk.types.machine import Machine

MachinePhase = str
OnStatus = Callable[[Machine], None]

TERMINAL_PHASES = frozenset({"failed", "destroyed"})


class MachineWaitError(Exception):
    """Raised when waiting for a machine fails or times out."""


class MachineTerminalError(MachineWaitError):
    """Machine reached a terminal phase (failed / destroyed)."""

    def __init__(self, machine_id: str, phase: str, last_error: Optional[str] = None):
        self.machine_id = machine_id
        self.phase = phase
        self.last_error = last_error
        msg = f"Machine {machine_id} reached terminal phase '{phase}'"
        if last_error:
            msg = f"{msg}: {last_error}"
        super().__init__(msg)


class MachineWaitTimeout(MachineWaitError):
    """Timed out while waiting for a machine phase."""

    def __init__(self, machine_id: str, timeout: float, last_phase: str):
        self.machine_id = machine_id
        self.timeout = timeout
        self.last_phase = last_phase
        super().__init__(
            f"Timed out waiting for machine {machine_id} after {timeout:.1f}s "
            f"(last phase: {last_phase})"
        )


def wait_until(
    client: Dedalus,
    machine_id: str,
    *,
    predicate: Callable[[Machine], bool],
    timeout: float = 120.0,
    poll_interval: float = 1.5,
    on_status: Optional[OnStatus] = None,
) -> Machine:
    """Poll until ``predicate(machine)`` is true.

    Raises:
        MachineTerminalError: if phase is ``failed`` or ``destroyed``
        MachineWaitTimeout: if ``timeout`` is exceeded
    """
    deadline = time.monotonic() + timeout

    machine = client.machines.retrieve(machine_id=machine_id)
    if on_status:
        on_status(machine)
    if predicate(machine):
        return machine

    while True:
        phase = getattr(machine.status, "phase", None) or ""
        if phase in TERMINAL_PHASES:
            last_error = getattr(machine.status, "last_error", None)
            raise MachineTerminalError(machine_id, phase, last_error)

        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise MachineWaitTimeout(machine_id, timeout, phase)

        time.sleep(min(poll_interval, remaining))

        machine = client.machines.retrieve(machine_id=machine_id)
        if on_status:
            on_status(machine)
        if predicate(machine):
            return machine


def wait_until_running(
    client: Dedalus,
    machine_id: str,
    *,
    timeout: float = 120.0,
    poll_interval: float = 1.5,
    on_status: Optional[OnStatus] = None,
) -> Machine:
    """Wait until ``status.phase == "running"``."""
    return wait_until(
        client,
        machine_id,
        predicate=lambda m: getattr(m.status, "phase", None) == "running",
        timeout=timeout,
        poll_interval=poll_interval,
        on_status=on_status,
    )


def wait_until_phase(
    client: Dedalus,
    machine_id: str,
    phase: Union[str, Sequence[str]],
    *,
    timeout: float = 120.0,
    poll_interval: float = 1.5,
    on_status: Optional[OnStatus] = None,
) -> Machine:
    """Wait until the machine reaches one of the given phases."""
    phases = {phase} if isinstance(phase, str) else set(phase)
    return wait_until(
        client,
        machine_id,
        predicate=lambda m: getattr(m.status, "phase", None) in phases,
        timeout=timeout,
        poll_interval=poll_interval,
        on_status=on_status,
    )


def create_and_wait(
    client: Dedalus,
    *,
    memory_mib: int,
    storage_gib: int,
    vcpu: Union[int, float],
    autosleep: Optional[str] = None,
    timeout: float = 120.0,
    poll_interval: float = 1.5,
    on_status: Optional[OnStatus] = None,
    **create_kwargs: Any,
) -> Machine:
    """Create a machine and wait until it is running.

    Extra keyword args are forwarded to ``client.machines.create``.
    """
    params: dict[str, Any] = {
        "memory_mib": memory_mib,
        "storage_gib": storage_gib,
        "vcpu": vcpu,
        **create_kwargs,
    }
    if autosleep is not None:
        params["autosleep"] = autosleep

    machine = client.machines.create(**params)
    return wait_until_running(
        client,
        machine.machine_id,
        timeout=timeout,
        poll_interval=poll_interval,
        on_status=on_status,
    )
