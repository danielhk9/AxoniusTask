import signal
import pytest

class SuiteTimeoutPlugin:
    def __init__(self, timeout):
        self.timeout = timeout

    def _timeout_handler(self, signum, frame):
        pytest.exit(f"\nTest suite exceeded timeout of {self.timeout} seconds.\n")

    def start_timer(self):
        if self.timeout:
            signal.signal(signal.SIGALRM, self._timeout_handler)
            signal.alarm(self.timeout)

    def cancel_timer(self):
        signal.alarm(0)

def pytest_addoption(parser):
    parser.addoption(
        "--suite-timeout",
        type=int,
        default=None,
        help="Fail the entire test suite if it runs longer than the specified timeout (in seconds)."
    )

def pytest_configure(config):
    timeout = config.getoption("--suite-timeout")
    plugin = SuiteTimeoutPlugin(timeout)
    config.pluginmanager.register(plugin, name="suite-timeout-plugin")
    plugin.start_timer()
    config._suite_timeout_plugin = plugin

def pytest_unconfigure(config):
    plugin = getattr(config, "_suite_timeout_plugin", None)
    if plugin:
        plugin.cancel_timer()
