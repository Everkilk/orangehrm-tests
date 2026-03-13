import pytest

from pages.pim_page import PIMPage


class TestPIMPage:
    @pytest.fixture
    def page(self, logged_in_driver):
        return PIMPage(logged_in_driver)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_verify_pim_menu_navigation(self, page):
        page.menu_click_pim_page()
        assert page.current_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_verify_add_button_opens_add_employee_page(self, page):
        page.menu_click_pim_page()
        page.click_add_button()
        assert page.current_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_employee_by_name(self, page):
        page.menu_click_pim_page()
        page.enter_employee_name("Linda")
        page.click_search_button()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_employee_by_id(self, page):
        page.menu_click_pim_page()
        page.enter_employee_id("0012")
        page.click_search_button()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_select_job_title(self, page):
        page.menu_click_pim_page()
        page.select_job_title("Software Engineer")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_select_employment_status(self, page):
        page.menu_click_pim_page()
        page.select_employment_status("Full-Time Permanent")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_select_include_option(self, page):
        page.menu_click_pim_page()
        page.select_include_option("Current Employees Only")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_select_sub_unit(self, page):
        page.menu_click_pim_page()
        page.select_sub_unit("Engineering")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_supervisor_name_search(self, page):
        page.menu_click_pim_page()
        page.enter_supervisor_name("Peter")
        page.click_search_button()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_reset_search_filters(self, page):
        page.menu_click_pim_page()
        page.enter_employee_name("John")
        page.enter_employee_id("0050")
        page.click_reset_button()
