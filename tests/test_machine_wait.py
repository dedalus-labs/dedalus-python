from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from dedalus_sdk.lib.machine_wait import (
    MachineTerminalError,
    MachineWaitTimeout,
    wait_until,
    wait_until_running,
)


def _machine(phase: str, last_error: str | None = None):
    status = SimpleNamespace(
        phase=phase,
        reason=phase,
        last_error=last_error,
    )
    return SimpleNamespace(machine_id="dm-test", status=status)


def test_wait_until_running_succeeds():
    phases = ["accepted", "starting", "running"]
    client = MagicMock()
    client.machines.retrieve.side_effect = [_machine(p) for p in phases]

    result = wait_until_running(client, "dm-test", poll_interval=0.01, timeout=2.0)
    assert result.status.phase == "running"
    assert client.machines.retrieve.call_count == 3


def test_wait_until_terminal_failed():
    client = MagicMock()
    client.machines.retrieve.return_value = _machine("failed", last_error="no capacity")

    with pytest.raises(MachineTerminalError) as ei:
        wait_until(
            client,
            "dm-test",
            predicate=lambda m: m.status.phase == "running",
            poll_interval=0.01,
            timeout=1.0,
        )
    assert "failed" in str(ei.value)
    assert "no capacity" in str(ei.value)


def test_wait_until_timeout():
    client = MagicMock()
    client.machines.retrieve.return_value = _machine("starting")

    with pytest.raises(MachineWaitTimeout):
        wait_until_running(client, "dm-test", poll_interval=0.01, timeout=0.05)
