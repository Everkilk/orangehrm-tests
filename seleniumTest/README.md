# OrangeHRM Selenium Python Framework

This project is a Python Selenium tests for OrangeHRM using:
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
