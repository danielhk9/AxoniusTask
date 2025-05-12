from setuptools import setup

setup(
    name="pytest-suite-timeout",
    py_modules=["pytest_suite_timeout"],
    entry_points={"pytest11": ["suite_timeout = pytest_suite_timeout"]},
    version="0.1",
    description="A plugin to enforce a max suite runtime in Pytest.",
    classifiers=["Framework :: Pytest"],
)
