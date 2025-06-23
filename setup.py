from setuptools import setup, find_packages

setup(
    name="pytest-suite-timeout",
    version="0.1",
    description="A Pytest plugin to enforce a maximum runtime for a test suite.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),  # This looks for __init__.py inside folders
    entry_points={
        "pytest11": [
            "suite_timeout = pytest_suite_timeout.plugin",
        ]
    },
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)