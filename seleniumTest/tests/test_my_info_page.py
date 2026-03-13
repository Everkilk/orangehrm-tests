import pytest

from pages.my_info_page import MyInfoPage


class TestMyInfoPage:
    @pytest.fixture
    def page(self, logged_in_driver):
        my_info_page = MyInfoPage(logged_in_driver)
        my_info_page.open_module()
        return my_info_page

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_and_open_my_info(self, logged_in_driver):
        assert logged_in_driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        page = MyInfoPage(logged_in_driver)
        page.open_module()
        assert page.is_loaded()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_enter_first_name(self, page):
        page.enter_first_name("John")
        assert page.get_first_name_value() == "John"

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_enter_middle_name(self, page):
        page.enter_middle_name("Paul")
        assert page.get_middle_name_value() == "Paul"

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_enter_last_name(self, page):
        page.enter_last_name("Doe")
        assert page.get_last_name_value() == "Doe"

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_select_date_of_birth(self, page):
        page.select_date_of_birth("1990-08-08")
        assert "08" in page.get_date_of_birth_value()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_select_dropdown_option(self, page):
        page.select_dropdown_option()
        assert page.get_dropdown_selected_value() is not None

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_click_button(self, page):
        page.click_button()
        assert "viewPersonalDetails" in page.get_current_page_url()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_set_blood_group(self, page):
        page.set_blood_group()
        assert page.get_blood_group_value() == "A+"

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_submit_form(self, page):
        page.submit_form()
        assert "viewPersonalDetails" in page.get_current_page_url()
