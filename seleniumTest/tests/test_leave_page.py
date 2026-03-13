import pytest

from pages.leave_page import LeavePage


class TestLeavePage:
    @pytest.fixture
    def page(self, logged_in_driver):
        logged_in_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")
        return LeavePage(logged_in_driver)

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_click_the_leave_menu(self, page):
        page.open_module()
        assert "leave/viewLeaveList" in page.current_url()

    @pytest.mark.regression
    def test_enter_the_leave_list(self, page):
        page.enter_from_date("2025-07-01")
        page.enter_to_date("2025-07-03")
        page.select_leave_status("Cancelled")
        page.select_leave_status("CAN - Personal")
        page.enter_employee_name("John")
        page.select_sub_unit("Engineering")
        assert page.click_search_button() is True

    @pytest.mark.regression
    def test_click_the_reset_button(self, page):
        page.enter_from_date("2025-07-01")
        page.enter_to_date("2025-07-03")
        page.select_leave_status("Cancelled")
        page.select_leave_status("CAN - Personal")
        page.enter_employee_name("John")
        page.select_sub_unit("Engineering")
        assert page.click_reset_button() is True

    @pytest.mark.sanity
    def test_from_date_field_is_empty(self, page):
        from_date_empty = page.enter_from_date("")
        assert from_date_empty == ""
        assert page.click_reset_button() is True

    @pytest.mark.sanity
    def test_to_date_field_is_empty(self, page):
        page.enter_from_date("2025-07-01")
        to_date_empty = page.enter_to_date("")
        assert to_date_empty == ""
        assert page.click_reset_button() is True

    @pytest.mark.regression
    def test_status_field_is_empty(self, page):
        page.enter_from_date("2025-07-01")
        page.enter_to_date("2025-07-03")
        leave_status_empty = page.select_leave_status("")
        assert leave_status_empty == ""
        assert page.click_reset_button() is True

    @pytest.mark.regression
    def test_fields_are_empty(self, page):
        from_date_empty = page.enter_from_date("")
        assert from_date_empty == ""
        to_date_empty = page.enter_to_date("")
        assert to_date_empty == ""
        leave_status_empty = page.select_leave_status("")
        assert leave_status_empty == ""
        assert page.click_reset_button() is True
