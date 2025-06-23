# Axonius E2E Automation Tests

End-to-end tests using Playwright and Pytest.  
Includes a custom plugin to limit total test suite runtime (`--suite-timeout`).  
Can be run locally or inside Docker.

---

## What's included

- Playwright for browser automation
- Pytest for test management
- Custom Pytest plugin (`suite_timeout`)
- Docker support
- Makefile and scripts for easy execution

---

## Getting started

### Clone the repo

```bash
git clone https://github.com/danielhk9/AxoniusTask.git
cd AxoniusTask
pytest e2e_tests/tests --suite-timeout=600
```

## run locally
```
bash install_local.sh
source .venv/bin/activate
pytest e2e_tests/tests --suite-timeout=900ests --suite-timeout=900
```
## Build the Docker image:
```
docker build -t axonius-tests .
docker run --rm axonius-tests --suite-timeout=900
```

## Run tests with Makefile
```
make build      # Build the Docker image
make run        # Run the tests inside Docker
```
