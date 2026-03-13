import pytest

from pages.admin_page import AdminPage


class TestAdminPage:
    @pytest.fixture
    def page(self, logged_in_driver):
        admin_page = AdminPage(logged_in_driver)
        admin_page.click_the_admin_menu()
        return admin_page

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_validation_and_open_admin(self, logged_in_driver):
        assert logged_in_driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        admin_page = AdminPage(logged_in_driver)
        admin_page.click_the_admin_menu()

    @pytest.mark.regression
    def test_search_system_users(self, page):
        page.enter_username_for_system_user("Admin")
        page.click_search_button_for_system_user()
        page.click_reset_button_for_system_user()

    @pytest.mark.regression
    def test_search_system_role(self, page):
        page.select_user_role_for_system_user("Admin")
        page.click_search_button_for_system_user()
        page.click_reset_button_for_system_user()

    @pytest.mark.regression
    def test_search_system_employee_name(self, page):
        page.enter_employee_name_for_system_user("John Doe")
        page.click_search_button_for_system_user()
        page.click_reset_button_for_system_user()

    @pytest.mark.regression
    def test_search_system_status(self, page):
        page.select_status_for_system_user("Enabled")
        page.click_search_button_for_system_user()
        page.click_reset_button_for_system_user()

    @pytest.mark.sanity
    def test_click_add_user_button(self, page):
        page.click_add_button_for_system_user()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_user(self, page):
        page.click_add_button_for_system_user()
        page.select_user_role("Admin")
        page.enter_employee_name("John Doe")
        page.select_status("Enabled")
        page.enter_username("john.doe")
        page.enter_password("Password123")
        page.enter_confirm_password("Password123")
        page.click_save_button()
