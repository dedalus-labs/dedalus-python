"""Create a Dedalus Machine and wait until it is running.

Usage:
    export DEDALUS_API_KEY=...
    python examples/create_and_wait_machine.py
"""

from __future__ import annotations

import os
import sys

from dedalus_sdk import Dedalus
from dedalus_sdk.lib.machine_wait import create_and_wait, MachineWaitError


def main() -> int:
    if not os.environ.get("DEDALUS_API_KEY") and not os.environ.get("DEDALUS_X_API_KEY"):
        print("Set DEDALUS_API_KEY (or DEDALUS_X_API_KEY) first.", file=sys.stderr)
        return 1

    client = Dedalus()

    print("Creating machine and waiting until running...")
    try:
        machine = create_and_wait(
            client,
            memory_mib=2048,
            storage_gib=10,
            vcpu=1,
            on_status=lambda m: print(f"  phase={m.status.phase} reason={m.status.reason}"),
        )
    except MachineWaitError as exc:
        print(f"Failed: {exc}", file=sys.stderr)
        return 1

    print(f"Ready: {machine.machine_id} ({machine.status.phase})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
