from setuptools import setup, find_packages

setup(
    name="pytest-suite-timeout",
    version="0.1",
    description="A Pytest plugin to enforce a maximum runtime per test suite.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="."),
    entry_points={
        "pytest11": [
            "suite_timeout = suite_timeout.plugin",
        ]
    },
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)