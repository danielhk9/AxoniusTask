import threading
import os
import sys

def pytest_addoption(parser):
    parser.addoption(
        "--suite-timeout",
        type=int,
        default=None,
        help="Fail the entire test suite if it runs longer than the specified timeout (in seconds)."
    )

def pytest_sessionstart(session):
    timeout = session.config.getoption("--suite-timeout")
    if timeout:
        def timeout_handler():
            print(f"\n\n⛔️ Test suite exceeded timeout of {timeout} seconds. Forcing failure...\n", file=sys.stderr)
            os._exit(1)  # Forcefully kill the test process

        # Start background timer
        timer = threading.Timer(timeout, timeout_handler)
        timer.daemon = True
        timer.start()
        session.timeout_timer = timer

def pytest_sessionfinish(session):
    timer = getattr(session, 'timeout_timer', None)
    if timer:
        timer.cancel()
