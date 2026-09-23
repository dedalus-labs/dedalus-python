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
    machine = client.machines.create(
        autosleep="300s",
        memory_mib=4096,
        storage_gib=10,
        vcpu=1,
        idempotency_key="",
    )


def _smoke_case_2() -> None:
    machine = client.machines.retrieve(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    )


def _smoke_case_3() -> None:
    machine = client.machines.update(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        idempotency_key="",
    )


def _smoke_case_4() -> None:
    machine = client.machines.update(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        autosleep="",
        memory_mib=0,
        storage_gib=0,
        vcpu=0,
        idempotency_key="",
    )


def _smoke_case_5() -> None:
    machine = client.machines.delete(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        idempotency_key="",
    )


def _smoke_case_6() -> None:
    machine = client.machines.sleep(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        idempotency_key="",
    )


def _smoke_case_7() -> None:
    machine = client.machines.wake(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        idempotency_key="",
    )


def _smoke_case_8() -> None:
    page = client.machines.ssh.list(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    )


def _smoke_case_9() -> None:
    ssh = client.machines.ssh.create(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        public_key="",
        idempotency_key="",
    )


def _smoke_case_10() -> None:
    ssh = client.machines.ssh.retrieve(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        session_id="sessionID",
    )


def _smoke_case_11() -> None:
    ssh = client.machines.ssh.delete(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        session_id="sessionID",
        idempotency_key="",
    )


def _smoke_case_12() -> None:
    page = client.machines.executions.list(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    )


def _smoke_case_13() -> None:
    execution = client.machines.executions.create(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        command=[""],
        idempotency_key="",
    )


def _smoke_case_14() -> None:
    execution = client.machines.executions.create(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        command=[""],
        cwd="",
        env={},
        stdin="",
        timeout_ms=0,
        idempotency_key="",
    )


def _smoke_case_15() -> None:
    execution = client.machines.executions.retrieve(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        execution_id="executionID",
    )


def _smoke_case_16() -> None:
    execution = client.machines.executions.delete(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        execution_id="executionID",
        idempotency_key="",
    )


def _smoke_case_17() -> None:
    execution = client.machines.executions.output(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        execution_id="executionID",
    )


def _smoke_case_18() -> None:
    page = client.machines.executions.events(
        machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        execution_id="executionID",
    )


def _smoke_case_19() -> None:
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


cases: list[SmokeCase] = [
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines",
        "run": _smoke_case_0,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines",
        "run": _smoke_case_1,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}",
        "run": _smoke_case_2,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/machines/{machine_id}",
        "label": "required params",
        "run": _smoke_case_3,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/machines/{machine_id}",
        "label": "all params",
        "run": _smoke_case_4,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}",
        "run": _smoke_case_5,
    },
    {
        "operation": "sleep",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/sleep",
        "run": _smoke_case_6,
    },
    {
        "operation": "wake",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/wake",
        "run": _smoke_case_7,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ssh",
        "run": _smoke_case_8,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/ssh",
        "run": _smoke_case_9,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/ssh/{session_id}",
        "run": _smoke_case_10,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/ssh/{session_id}",
        "run": _smoke_case_11,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions",
        "run": _smoke_case_12,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/executions",
        "label": "required params",
        "run": _smoke_case_13,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/machines/{machine_id}/executions",
        "label": "all params",
        "run": _smoke_case_14,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}",
        "run": _smoke_case_15,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}",
        "run": _smoke_case_16,
    },
    {
        "operation": "output",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}/output",
        "run": _smoke_case_17,
    },
    {
        "operation": "events",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/executions/{execution_id}/events",
        "run": _smoke_case_18,
    },
    {
        "operation": "connect",
        "method": "GET",
        "path": "/v1/machines/{machine_id}/terminals/{terminal_id}/stream",
        "run": _smoke_case_19,
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
