from core.base_page import BasePage


class MyInfoPage(BasePage):
    my_info_menu = BasePage.by_xpath("//span[text()='My Info']")
    my_info_header = BasePage.by_xpath("//h6[text()='Personal Details']")
    first_name = BasePage.by_name("firstName")
    middle_name = BasePage.by_name("middleName")
    last_name = BasePage.by_name("lastName")
    date_of_birth = BasePage.by_xpath("(//input[@placeholder='yyyy-dd-mm'])[1]")
    generic_select = BasePage.by_xpath("//*[text() = '-- Select --']")
    save_button = BasePage.by_css("button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
    blood_group_field = BasePage.by_xpath("(//label[text()='Blood Type']/following::div[contains(@class,'oxd-select-text-input')])[1]")
    blood_group_a_plus = BasePage.by_xpath("//*[text()='A+']")

    def open_module(self) -> None:
        self.click(self.my_info_menu)

    def is_loaded(self) -> bool:
        return self.is_visible(self.first_name)

    def current_name_fields(self) -> tuple[str, str, str]:
        first = self.driver.find_element(*self.first_name).get_attribute("value")
        middle = self.driver.find_element(*self.middle_name).get_attribute("value")
        last = self.driver.find_element(*self.last_name).get_attribute("value")
        return first, middle, last

    def enter_first_name(self, value: str) -> None:
        self.clear_and_type(self.first_name, value)

    def enter_middle_name(self, value: str) -> None:
        self.clear_and_type(self.middle_name, value)

    def enter_last_name(self, value: str) -> None:
        self.clear_and_type(self.last_name, value)

    def get_first_name_value(self) -> str:
        return self.driver.find_element(*self.first_name).get_attribute("value")

    def get_middle_name_value(self) -> str:
        return self.driver.find_element(*self.middle_name).get_attribute("value")

    def get_last_name_value(self) -> str:
        return self.driver.find_element(*self.last_name).get_attribute("value")

    def select_date_of_birth(self, value: str = "1990-08-08") -> None:
        self.clear_and_type(self.date_of_birth, value)

    def get_date_of_birth_value(self) -> str:
        return self.driver.find_element(*self.date_of_birth).get_attribute("value")

    def select_dropdown_option(self) -> None:
        self.click(self.generic_select)

    def get_dropdown_selected_value(self) -> str:
        return self.driver.find_element(*self.generic_select).text

    def click_button(self) -> None:
        self.click(self.save_button)

    def set_blood_group(self) -> None:
        self.click(self.blood_group_field)
        self.click(self.blood_group_a_plus)

    def get_blood_group_value(self) -> str:
        return self.driver.find_element(*self.blood_group_field).text

    def submit_form(self) -> None:
        self.click(self.save_button)

    def get_current_page_url(self) -> str:
        return self.current_url()
