# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from dedalus_sdk import Dedalus

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = Dedalus(max_retries=2, timeout=10)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    page = client.machines.list()


def _smoke_case_1() -> None:
    page = client.machines.list(
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_2() -> None:
    machine = client.machines.create(
        autosleep="300s",
        memory_mib=4096,
        storage_gib=10,
        vcpu=1,
        idempotency_key="",
    )


def _smoke_case_3() -> None:
    machine = client.machines.create(
        autosleep="300s",
        memory_mib=4096,
        storage_gib=10,
        vcpu=1,
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_4() -> None:
    machine = client.machines.retrieve(
        machine_id="machineID",
    )


def _smoke_case_5() -> None:
    machine = client.machines.retrieve(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_6() -> None:
    machine = client.machines.update(
        machine_id="machineID",
        idempotency_key="",
    )


def _smoke_case_7() -> None:
    machine = client.machines.update(
        machine_id="machineID",
        autosleep="",
        memory_mib=0,
        storage_gib=0,
        vcpu=0,
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_8() -> None:
    machine = client.machines.delete(
        machine_id="machineID",
        idempotency_key="",
    )


def _smoke_case_9() -> None:
    machine = client.machines.delete(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_10() -> None:
    stream = client.machines.watch(
        machine_id="machineID",
    )

    for machine in stream:
        print(machine)


def _smoke_case_11() -> None:
    stream = client.machines.watch(
        machine_id="machineID",
        x_dedalus_org_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        last_event_id="last_event_id",
    )

    for machine in stream:
        print(machine)


def _smoke_case_12() -> None:
    machine = client.machines.sleep(
        machine_id="machineID",
        idempotency_key="",
    )


def _smoke_case_13() -> None:
    machine = client.machines.sleep(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_14() -> None:
    machine = client.machines.wake(
        machine_id="machineID",
        idempotency_key="",
    )


def _smoke_case_15() -> None:
    machine = client.machines.wake(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_16() -> None:
    network = client.machines.network.retrieve(
        machine_id="machineID",
    )


def _smoke_case_17() -> None:
    network = client.machines.network.retrieve(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_18() -> None:
    page = client.machines.artifacts.list(
        machine_id="machineID",
    )


def _smoke_case_19() -> None:
    page = client.machines.artifacts.list(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_20() -> None:
    artifact = client.machines.artifacts.retrieve(
        machine_id="machineID",
        artifact_id="artifactID",
    )


def _smoke_case_21() -> None:
    artifact = client.machines.artifacts.retrieve(
        machine_id="machineID",
        artifact_id="artifactID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_22() -> None:
    artifact = client.machines.artifacts.delete(
        machine_id="machineID",
        artifact_id="artifactID",
        idempotency_key="",
    )


def _smoke_case_23() -> None:
    artifact = client.machines.artifacts.delete(
        machine_id="machineID",
        artifact_id="artifactID",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_24() -> None:
    page = client.machines.ports.list(
        machine_id="machineID",
    )


def _smoke_case_25() -> None:
    page = client.machines.ports.list(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_26() -> None:
    port = client.machines.ports.create(
        machine_id="machineID",
        port=0,
        idempotency_key="",
    )


def _smoke_case_27() -> None:
    port = client.machines.ports.create(
        machine_id="machineID",
        port=0,
        protocol="http",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_28() -> None:
    port = client.machines.ports.retrieve(
        machine_id="machineID",
        port_id="portID",
    )


def _smoke_case_29() -> None:
    port = client.machines.ports.retrieve(
        machine_id="machineID",
        port_id="portID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_30() -> None:
    port = client.machines.ports.delete(
        machine_id="machineID",
        port_id="portID",
        idempotency_key="",
    )


def _smoke_case_31() -> None:
    port = client.machines.ports.delete(
        machine_id="machineID",
        port_id="portID",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_32() -> None:
    page = client.machines.ssh.list(
        machine_id="machineID",
    )


def _smoke_case_33() -> None:
    page = client.machines.ssh.list(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_34() -> None:
    ssh = client.machines.ssh.create(
        machine_id="machineID",
        public_key="",
        idempotency_key="",
    )


def _smoke_case_35() -> None:
    ssh = client.machines.ssh.create(
        machine_id="machineID",
        public_key="",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_36() -> None:
    ssh = client.machines.ssh.retrieve(
        machine_id="machineID",
        session_id="sessionID",
    )


def _smoke_case_37() -> None:
    ssh = client.machines.ssh.retrieve(
        machine_id="machineID",
        session_id="sessionID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_38() -> None:
    ssh = client.machines.ssh.delete(
        machine_id="machineID",
        session_id="sessionID",
        idempotency_key="",
    )


def _smoke_case_39() -> None:
    ssh = client.machines.ssh.delete(
        machine_id="machineID",
        session_id="sessionID",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_40() -> None:
    page = client.machines.executions.list(
        machine_id="machineID",
    )


def _smoke_case_41() -> None:
    page = client.machines.executions.list(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_42() -> None:
    execution = client.machines.executions.create(
        machine_id="machineID",
        command=[""],
        idempotency_key="",
    )


def _smoke_case_43() -> None:
    execution = client.machines.executions.create(
        machine_id="machineID",
        command=[""],
        cwd="",
        env={},
        stdin="",
        timeout_ms=0,
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_44() -> None:
    execution = client.machines.executions.retrieve(
        machine_id="machineID",
        execution_id="executionID",
    )


def _smoke_case_45() -> None:
    execution = client.machines.executions.retrieve(
        machine_id="machineID",
        execution_id="executionID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_46() -> None:
    execution = client.machines.executions.delete(
        machine_id="machineID",
        execution_id="executionID",
        idempotency_key="",
    )


def _smoke_case_47() -> None:
    execution = client.machines.executions.delete(
        machine_id="machineID",
        execution_id="executionID",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_48() -> None:
    execution = client.machines.executions.output(
        machine_id="machineID",
        execution_id="executionID",
    )


def _smoke_case_49() -> None:
    execution = client.machines.executions.output(
        machine_id="machineID",
        execution_id="executionID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_50() -> None:
    page = client.machines.executions.events(
        machine_id="machineID",
        execution_id="executionID",
    )


def _smoke_case_51() -> None:
    page = client.machines.executions.events(
        machine_id="machineID",
        execution_id="executionID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_52() -> None:
    page = client.machines.terminals.list(
        machine_id="machineID",
    )


def _smoke_case_53() -> None:
    page = client.machines.terminals.list(
        machine_id="machineID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_54() -> None:
    terminal = client.machines.terminals.create(
        machine_id="machineID",
        height=0,
        width=0,
        idempotency_key="",
    )


def _smoke_case_55() -> None:
    terminal = client.machines.terminals.create(
        machine_id="machineID",
        cwd="",
        env={},
        height=0,
        shell="",
        width=0,
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_56() -> None:
    terminal = client.machines.terminals.retrieve(
        machine_id="machineID",
        terminal_id="terminalID",
    )


def _smoke_case_57() -> None:
    terminal = client.machines.terminals.retrieve(
        machine_id="machineID",
        terminal_id="terminalID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_58() -> None:
    terminal = client.machines.terminals.delete(
        machine_id="machineID",
        terminal_id="terminalID",
        idempotency_key="",
    )


def _smoke_case_59() -> None:
    terminal = client.machines.terminals.delete(
        machine_id="machineID",
        terminal_id="terminalID",
        x_dedalus_org_id="x_dedalus_org_id",
        idempotency_key="",
    )


def _smoke_case_60() -> None:
    def _probe() -> None:
        with client.machines.terminals.connect(
            machine_id="machineID",
            terminal_id="terminalID",
        ) as socket:
            try:
                socket.recv()
            finally:
                socket.close(code=1000, reason="smoke-test")

    _probe()


def _smoke_case_61() -> None:
    network = client.networks.retrieve(
        network_id="networkID",
    )


def _smoke_case_62() -> None:
    network = client.networks.retrieve(
        network_id="networkID",
        x_dedalus_org_id="x_dedalus_org_id",
    )


def _smoke_case_63() -> None:
    usage = client.usage.retrieve()


def _smoke_case_64() -> None:
    usage = client.usage.retrieve(
        period_start="period_start",
    )


def _smoke_case_65() -> None:
    usage = client.usage.machine_compute()


def _smoke_case_66() -> None:
    usage = client.usage.machine_compute(
        period_start="period_start",
        period_end="period_end",
        machine_id="machine_id",
        granularity="granularity",
    )


def _smoke_case_67() -> None:
    usage = client.usage.machine_storage()


def _smoke_case_68() -> None:
    usage = client.usage.machine_storage(
        period_start="period_start",
        period_end="period_end",
        machine_id="machine_id",
    )


cases: list[SmokeCase] = [
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines",
        "label": "required params",
        "run": _smoke_case_0,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines",
        "label": "all params",
        "run": _smoke_case_1,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines",
        "label": "required params",
        "run": _smoke_case_2,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines",
        "label": "all params",
        "run": _smoke_case_3,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}",
        "label": "required params",
        "run": _smoke_case_4,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}",
        "label": "all params",
        "run": _smoke_case_5,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/machines/{machine_id}",
        "label": "required params",
        "run": _smoke_case_6,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/machines/{machine_id}",
        "label": "all params",
        "run": _smoke_case_7,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}",
        "label": "required params",
        "run": _smoke_case_8,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}",
        "label": "all params",
        "run": _smoke_case_9,
    },
    {
        "operation": "watch",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/status/stream",
        "label": "required params",
        "run": _smoke_case_10,
    },
    {
        "operation": "watch",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/status/stream",
        "label": "all params",
        "run": _smoke_case_11,
    },
    {
        "operation": "sleep",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/sleep",
        "label": "required params",
        "run": _smoke_case_12,
    },
    {
        "operation": "sleep",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/sleep",
        "label": "all params",
        "run": _smoke_case_13,
    },
    {
        "operation": "wake",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/wake",
        "label": "required params",
        "run": _smoke_case_14,
    },
    {
        "operation": "wake",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/wake",
        "label": "all params",
        "run": _smoke_case_15,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/network",
        "label": "required params",
        "run": _smoke_case_16,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/network",
        "label": "all params",
        "run": _smoke_case_17,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/artifacts",
        "label": "required params",
        "run": _smoke_case_18,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/artifacts",
        "label": "all params",
        "run": _smoke_case_19,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/artifacts/{artifact_id}",
        "label": "required params",
        "run": _smoke_case_20,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/artifacts/{artifact_id}",
        "label": "all params",
        "run": _smoke_case_21,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/artifacts/{artifact_id}",
        "label": "required params",
        "run": _smoke_case_22,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/artifacts/{artifact_id}",
        "label": "all params",
        "run": _smoke_case_23,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ports",
        "label": "required params",
        "run": _smoke_case_24,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ports",
        "label": "all params",
        "run": _smoke_case_25,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/ports",
        "label": "required params",
        "run": _smoke_case_26,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/ports",
        "label": "all params",
        "run": _smoke_case_27,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ports/{port_id}",
        "label": "required params",
        "run": _smoke_case_28,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ports/{port_id}",
        "label": "all params",
        "run": _smoke_case_29,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/ports/{port_id}",
        "label": "required params",
        "run": _smoke_case_30,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/ports/{port_id}",
        "label": "all params",
        "run": _smoke_case_31,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ssh",
        "label": "required params",
        "run": _smoke_case_32,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ssh",
        "label": "all params",
        "run": _smoke_case_33,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/ssh",
        "label": "required params",
        "run": _smoke_case_34,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/ssh",
        "label": "all params",
        "run": _smoke_case_35,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ssh/{session_id}",
        "label": "required params",
        "run": _smoke_case_36,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ssh/{session_id}",
        "label": "all params",
        "run": _smoke_case_37,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/ssh/{session_id}",
        "label": "required params",
        "run": _smoke_case_38,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/ssh/{session_id}",
        "label": "all params",
        "run": _smoke_case_39,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions",
        "label": "required params",
        "run": _smoke_case_40,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions",
        "label": "all params",
        "run": _smoke_case_41,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/executions",
        "label": "required params",
        "run": _smoke_case_42,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/executions",
        "label": "all params",
        "run": _smoke_case_43,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}",
        "label": "required params",
        "run": _smoke_case_44,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}",
        "label": "all params",
        "run": _smoke_case_45,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}",
        "label": "required params",
        "run": _smoke_case_46,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}",
        "label": "all params",
        "run": _smoke_case_47,
    },
    {
        "operation": "output",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}/output",
        "label": "required params",
        "run": _smoke_case_48,
    },
    {
        "operation": "output",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}/output",
        "label": "all params",
        "run": _smoke_case_49,
    },
    {
        "operation": "events",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}/events",
        "label": "required params",
        "run": _smoke_case_50,
    },
    {
        "operation": "events",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}/events",
        "label": "all params",
        "run": _smoke_case_51,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/terminals",
        "label": "required params",
        "run": _smoke_case_52,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/terminals",
        "label": "all params",
        "run": _smoke_case_53,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/terminals",
        "label": "required params",
        "run": _smoke_case_54,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/terminals",
        "label": "all params",
        "run": _smoke_case_55,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/terminals/{terminal_id}",
        "label": "required params",
        "run": _smoke_case_56,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/terminals/{terminal_id}",
        "label": "all params",
        "run": _smoke_case_57,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/terminals/{terminal_id}",
        "label": "required params",
        "run": _smoke_case_58,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/terminals/{terminal_id}",
        "label": "all params",
        "run": _smoke_case_59,
    },
    {
        "operation": "connect",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/terminals/{terminal_id}/stream",
        "run": _smoke_case_60,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/networks/{network_id}",
        "label": "required params",
        "run": _smoke_case_61,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/networks/{network_id}",
        "label": "all params",
        "run": _smoke_case_62,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/usage",
        "label": "required params",
        "run": _smoke_case_63,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/usage",
        "label": "all params",
        "run": _smoke_case_64,
    },
    {
        "operation": "machineCompute",
        "method": "GET",
        "path": "/v1/usage/machines/compute",
        "label": "required params",
        "run": _smoke_case_65,
    },
    {
        "operation": "machineCompute",
        "method": "GET",
        "path": "/v1/usage/machines/compute",
        "label": "all params",
        "run": _smoke_case_66,
    },
    {
        "operation": "machineStorage",
        "method": "GET",
        "path": "/v1/usage/machines/storage",
        "label": "required params",
        "run": _smoke_case_67,
    },
    {
        "operation": "machineStorage",
        "method": "GET",
        "path": "/v1/usage/machines/storage",
        "label": "all params",
        "run": _smoke_case_68,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
