# Axonius E2E Automation Tests

This project includes end-to-end tests using **Playwright** and **Pytest**, wrapped with Docker and a custom Pytest plugin that makes sure test runs don’t go on forever (`--suite-timeout`). It's easy to run locally or in CI, and includes a Makefile and shell script to simplify things.

---

## 🔧 What’s inside

- Playwright for fast browser automation
- Pytest for test structure and fixtures
- A custom plugin to fail tests if the suite runs too long
- Docker support (build once, run anywhere)
- `Makefile` and `run_tests.sh` for quick execution

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/danielhk9/AxoniusTask.git
cd AxoniusTask
```

---

### 2. Run locally (Python 3.11+)

```bash
python -m venv .venv
source .venv/Scripts/activate        # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install
pytest e2e_tests/tests --suite-timeout=900
```

---
## 🧩 Plugin: --suite-timeout

The `--suite-timeout` flag lets you define a max number of seconds for the full test suite. If it runs longer than that, the rest of the tests will fail.

### 3. Run with Docker

#### Build the image

```bash
docker build -t axonius-tests .
```

#### Run the tests

```bash
docker run --rm axonius-tests --suite-timeout=900 --log-level=DEBUG
```


### 4. Use the Makefile (Optional)

#### Build + run:

```bash
make build
make test
make repeat- will execute 10 times 
```

---

## 📁 Project Structure

```
.
├── e2e_tests/
│   ├── tests/                # Actual tests
│   ├── pages/                # Page-related helper functions
│   ├── constants/            # Selectors and test data
│   └── conftest.py
├── pytest_suite_timeout/     # Custom plugin (suite timeout)
├── run_tests.sh              # Test runner script
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```

