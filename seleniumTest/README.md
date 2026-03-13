# OrangeHRM Selenium Python Framework

This project is a Python migration of key OrangeHRM Selenium tests using:
- Selenium WebDriver
- pytest
- pytest-html reporting
- Page Object Model (POM)

## Covered Modules (6 test files)
- tests/test_login_page.py
- tests/test_dashboard_page.py
- tests/test_leave_page.py
- tests/test_pim_page.py
- tests/test_admin_page.py
- tests/test_my_info_page.py

## Project Structure
- config: environment and credential config
- core: driver creation and base page wrapper
- pages: page object classes for each module
- data: test datasets for data-driven testing
- tests: executable pytest test cases
- utils: screenshot helper and utilities
- reports: HTML report and failure screenshots

## Setup
1. Create and activate virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run all tests

```bash
pytest
```

## Run only smoke tests

```bash
pytest -m smoke
```

## Run one module

```bash
pytest tests/test_login_page.py
```

## Report Output
After run, HTML report is generated at:
- reports/report.html

Screenshots for failed tests are saved under:
- reports/screenshots/
