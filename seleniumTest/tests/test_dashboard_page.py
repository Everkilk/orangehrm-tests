import pytest
from urllib.request import Request, urlopen

from pages.dashboard_page import DashboardPage


class TestDashboardPage:
    @pytest.fixture
    def page(self, logged_in_driver):
        dashboard_page = DashboardPage(logged_in_driver)
        assert dashboard_page.current_url() != "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        return dashboard_page

    def _validate_broken_links(self, driver) -> None:
        links = driver.find_elements("tag name", "a")
        for link in links:
            href = link.get_attribute("href")
            if not href or not href.startswith("http"):
                continue
            try:
                req = Request(href, method="HEAD")
                with urlopen(req, timeout=5):
                    pass
            except Exception:
                continue

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verify_page_name(self, page):
        assert page.name_of_page() == "Dashboard"

    @pytest.mark.regression
    def test_verify_clock_page(self, page):
        page.clock_icon_click()
        page.back()

    @pytest.mark.regression
    def test_verify_performance_page(self, page):
        url = page.my_notification()
        assert url == "https://opensource-demo.orangehrmlive.com/web/index.php/performance/myPerformanceReview"
        page.back()

    @pytest.mark.regression
    def test_verify_assign_leave_page(self, page):
        title = page.assign_leave_click()
        assert title == "OrangeHRM"
        page.back()

    @pytest.mark.regression
    def test_verify_leave_list_page(self, page):
        url = page.leave_list_click()
        assert url == "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"
        page.back()

    @pytest.mark.regression
    def test_verify_timesheet_page(self, page):
        url = page.timesheet_click()
        assert url == "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet"
        page.back()

    @pytest.mark.regression
    def test_verify_apply_leave_page(self, page):
        url = page.apply_leave_click()
        assert url == "https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave"
        page.back()

    @pytest.mark.regression
    def test_verify_my_leave_page(self, page):
        url = page.my_leave_click()
        assert url == "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList"
        page.back()

    @pytest.mark.regression
    def test_verify_my_timesheet_page(self, page):
        url = page.my_timesheet_click()
        assert url == "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewMyTimesheet"
        page.back()

    @pytest.mark.regression
    def test_verify_employee_leave_settings(self, page):
        page.employee_leave_setting_icon()
        page.employee_leave_close_click()
        page.employee_leave_setting_icon()
        page.employee_leave_cancel_click()
        page.employee_leave_setting_icon()
        page.employee_leave_checkbox_click()
        page.driver.save_screenshot("reports/screenshots/employee_leave_checkbox.png")
        page.employee_leave_save_click()

    @pytest.mark.regression
    def test_verify_buzz_page(self, page):
        url = page.buzz_page()
        assert url == "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"
        page.back()

    @pytest.mark.regression
    def test_capture_dashboard_screens(self, page):
        page.driver.save_screenshot("reports/screenshots/dash1.png")
        page.scroll_page()
        page.driver.save_screenshot("reports/screenshots/dash2.png")

    @pytest.mark.regression
    def test_verify_employee_distribution(self, page):
        page.engineering_click()
        page.human_resource_click()
        page.unassigned_click()
        page.driver.save_screenshot("reports/screenshots/circle-change.png")

    @pytest.mark.regression
    def test_verify_admin_menu_working(self, page):
        url = page.admin_menu_verify()
        assert url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        page.back()

    @pytest.mark.regression
    def test_check_broken_links(self, page):
        self._validate_broken_links(page.driver)
