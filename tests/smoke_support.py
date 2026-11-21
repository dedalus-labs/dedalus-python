# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Shared by every smoke test under `tests/`. Each test calls one SDK method the way the SDK
# exposes it, against the server named by TEST_API_BASE_URL:
#
#   TEST_API_BASE_URL=http://localhost:4010 python -m pytest
#
# Environment variables:
#   - TEST_API_BASE_URL: the server to call. Unset, every smoke test skips, so a plain `pytest`
#     never calls the real API. Credentials come from the variables the client itself reads.
#   - SCALAR_SMOKE_FILTER: comma-separated needles; only cases whose operation name or path
#     contains one of them run. Empty means no filter.
#   - SCALAR_SMOKE_REPORT_DIR: a directory; each test process appends one JSON line per case it
#     ran to its own file there. The generator uses this to collect per-case results.
#
# Regeneration does not yet delete a test module whose resource was renamed or removed. Delete a
# stale module under `tests/api_resources/` by hand, or `pytest` keeps running it.
from __future__ import annotations

import functools
import json
import os
import secrets
import threading
import time
import traceback
from typing import Any, Callable, TypeVar, cast

import pytest

from dedalus_sdk import Dedalus

# Fingerprint of the case list the generator's smoke runner checks this suite against (written only
# for generator tooling). The runner refuses a list whose digest differs, so a list left by an
# earlier generation is never trusted.
SMOKE_CASE_LIST_DIGEST = "ba9877f69295ef0d"

_BASE_URL = os.environ.get("TEST_API_BASE_URL") or None

# The client every smoke test calls through. It is built only for a smoke run: the constructor
# raises when a credential the client requires is missing, and a plain `pytest` without
# credentials must still import every test module, where each case then skips before touching it.
# Retries and the per-attempt timeout are stated rather than inherited, because the client
# defaults are config-derived and can be zero retries; three 10s attempts plus backoff fit inside
# the 35s case bound below.
client: Dedalus = Dedalus(base_url=_BASE_URL, max_retries=2, timeout=10) if _BASE_URL else cast("Dedalus", None)

_NEEDLES = [needle.strip() for needle in os.environ.get("SCALAR_SMOKE_FILTER", "").split(",") if needle.strip()]

_REPORT_DIR = os.environ.get("SCALAR_SMOKE_REPORT_DIR") or None
# One file per process: no two writers ever share a file, and the lock below keeps the appends of
# one process from interleaving, so nothing relies on append atomicity.
_REPORT_FILE = os.path.join(_REPORT_DIR, f"{os.getpid()}-{secrets.token_hex(8)}.jsonl") if _REPORT_DIR else None
_REPORT_LOCK = threading.Lock()

# How long one case may take, all retries included, before it is recorded as failed. pytest has
# no per-test timeout of its own, so this is the case's only bound.
CASE_BOUND_SECONDS = 35.0

_Test = TypeVar("_Test", bound=Callable[..., None])


def _is_selected(operation: str, path: str) -> bool:
    """Whether the filter selects a case: no needles, or one contained in its operation or path."""
    return not _NEEDLES or any(needle in operation or needle in path for needle in _NEEDLES)


def _record(line: dict[str, Any]) -> None:
    """Appends one result line to this process's report file, when the generator asked for one."""
    if _REPORT_FILE is None:
        return
    with _REPORT_LOCK, open(_REPORT_FILE, "a", encoding="utf-8") as report:
        report.write(json.dumps(line) + "\n")


def _run_bounded(body: Callable[[], None]) -> None:
    """Runs a case body, raising once it has run longer than the case bound."""
    # A daemon thread, so a call that never returns (an unanswered WebSocket read) can neither block
    # the next case nor keep the process alive at exit.
    outcome: list[BaseException] = []

    def target() -> None:
        try:
            body()
        except BaseException as error:  # handed back to the test thread below
            outcome.append(error)

    worker = threading.Thread(target=target, daemon=True)
    worker.start()
    worker.join(CASE_BOUND_SECONDS)
    if worker.is_alive():
        raise TimeoutError(f"The case did not finish within {CASE_BOUND_SECONDS:g} s.")
    if outcome:
        raise outcome[0]


def smoke_case(case_id: str, *, operation: str, path: str) -> Callable[[_Test], _Test]:
    """Marks a test method as one smoke case.

    `case_id` is the stable id the result is recorded under, and `operation` and `path` are the
    fields the filter matches. A failure is recorded and then re-raised, so pytest sees it too.
    """

    def decorate(test: _Test) -> _Test:
        @functools.wraps(test)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            if not _BASE_URL:
                pytest.skip("TEST_API_BASE_URL is not set")
            if not _is_selected(operation, path):
                pytest.skip("not selected by SCALAR_SMOKE_FILTER")
            started_at = time.monotonic()
            try:
                _run_bounded(lambda: test(*args, **kwargs))
            except Exception:
                duration_ms = int((time.monotonic() - started_at) * 1000)
                _record({"id": case_id, "status": "failed", "durationMs": duration_ms, "error": traceback.format_exc()})
                raise
            _record({"id": case_id, "status": "passed", "durationMs": int((time.monotonic() - started_at) * 1000)})

        return cast("_Test", wrapper)

    return decorate
