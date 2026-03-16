# OrangeHRM Selenium với Pytest

 Thực hiện test auto OrangeHRM bằng Python Selenium, sử dụng:
- Selenium WebDriver
- pytest
- báo cáo pytest-html
- Mô hình Page Object Model (POM)

## Các module đã cover (6 file test)
- tests/test_login_page.py
- tests/test_dashboard_page.py
- tests/test_leave_page.py
- tests/test_pim_page.py
- tests/test_admin_page.py
- tests/test_my_info_page.py

## Cấu trúc dự án
- config: cấu hình môi trường và thông tin đăng nhập
- core: khởi tạo driver và lớp base page wrapper
- pages: các class Page Object cho từng module
- data: dữ liệu test phục vụ data-driven testing
- tests: các test case pytest có thể chạy trực tiếp
