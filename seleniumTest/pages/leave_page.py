from core.base_page import BasePage


class LeavePage(BasePage):
    leave_menu = BasePage.by_xpath("//span[text()='Leave']")
    leave_header = BasePage.by_xpath("//h6[text()='Leave']")
    from_date = BasePage.by_xpath("(//input[starts-with(@placeholder,'yyyy')])[1]")
    to_date = BasePage.by_xpath("(//input[@placeholder='yyyy-dd-mm'])[2]")
    leave_status_dropdown = BasePage.by_xpath("(//div[@class='oxd-select-text-input'])[1]")
    employee_name = BasePage.by_xpath("//input[@placeholder='Type for hints...']")
    sub_unit_dropdown = BasePage.by_xpath("(//div[@class='oxd-select-text-input'])[3]")
    search_button = BasePage.by_xpath("(//button[contains(@class,'oxd-button--medium')])[2]")
    reset_button = BasePage.by_xpath("(//button[contains(@class,'oxd-button--medium')])[1]")

    def open_module(self) -> None:
        self.click(self.leave_menu)

    def is_loaded(self) -> bool:
        return self.is_visible(self.leave_header)

    def search_by_date(self, from_date_value: str, to_date_value: str) -> None:
        self.type(self.from_date, from_date_value)
        self.type(self.to_date, to_date_value)
        self.click(self.search_button)

    def enter_from_date(self, date_value: str) -> str:
        self.clear_and_type(self.from_date, date_value)
        return self.driver.find_element(*self.from_date).get_attribute("value")

    def enter_to_date(self, date_value: str) -> str:
        self.clear_and_type(self.to_date, date_value)
        return self.driver.find_element(*self.to_date).get_attribute("value")

    def select_leave_status(self, status_value: str) -> str:
        if not status_value:
            return ""
        self.click(self.leave_status_dropdown)
        self.click_xpath_text("span", status_value)
        return self.driver.find_element(*self.leave_status_dropdown).text

    def enter_employee_name(self, name: str) -> None:
        self.clear_and_type(self.employee_name, name)

    def select_sub_unit(self, sub_unit: str) -> None:
        self.click(self.sub_unit_dropdown)
        self.click_xpath_text("span", sub_unit)

    def click_search_button(self) -> bool:
        self.click(self.search_button)
        return True

    def click_reset_button(self) -> bool:
        self.click(self.reset_button)
        return True
