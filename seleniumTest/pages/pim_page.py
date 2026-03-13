from core.base_page import BasePage


class PIMPage(BasePage):
    pim_menu = BasePage.by_xpath("//span[text()='PIM']")
    pim_header = BasePage.by_xpath("//h6[text()='PIM']")
    employee_name_input = BasePage.by_xpath("(//input[@placeholder='Type for hints...'])[1]")
    employee_id_input = BasePage.by_xpath("(//input[contains(@class,'oxd-input--active')])[2]")
    search_button = BasePage.by_xpath("//button[@type='submit' and contains(.,'Search')]")
    reset_button = BasePage.by_xpath("//button[@type='reset' and contains(.,'Reset')]")
    add_button = BasePage.by_xpath("//div[@class='orangehrm-header-container']//button[contains(.,'Add')]")
    job_title_dropdown = BasePage.by_xpath("(//div[@class='oxd-select-text-input'])[1]")
    employment_status_dropdown = BasePage.by_xpath("(//div[@class='oxd-select-text-input'])[2]")
    include_dropdown = BasePage.by_xpath("(//div[@class='oxd-select-text-input'])[3]")
    sub_unit_dropdown = BasePage.by_xpath("(//div[@class='oxd-select-text-input'])[4]")
    supervisor_name_input = BasePage.by_xpath("(//input[@placeholder='Type for hints...'])[2]")

    def open_module(self) -> None:
        self.click(self.pim_menu)

    def is_loaded(self) -> bool:
        return self.is_visible(self.pim_header)

    def search_employee(self, employee_name: str) -> None:
        self.type(self.employee_name_input, employee_name)
        self.click(self.search_button)

    def menu_click_pim_page(self) -> None:
        self.click(self.pim_menu)

    def click_add_button(self) -> None:
        self.click(self.add_button)

    def enter_employee_name(self, employee_name: str) -> None:
        self.clear_and_type(self.employee_name_input, employee_name)

    def enter_employee_id(self, employee_id: str) -> None:
        self.clear_and_type(self.employee_id_input, employee_id)

    def select_job_title(self, job_title: str) -> None:
        self.click(self.job_title_dropdown)
        self.click_xpath_text("span", job_title)

    def select_employment_status(self, status: str) -> None:
        self.click(self.employment_status_dropdown)
        self.click_xpath_text("span", status)

    def select_include_option(self, option: str) -> None:
        self.click(self.include_dropdown)
        self.click_xpath_text("span", option)

    def select_sub_unit(self, sub_unit: str) -> None:
        self.click(self.sub_unit_dropdown)
        self.click_xpath_text("span", sub_unit)

    def enter_supervisor_name(self, supervisor_name: str) -> None:
        self.clear_and_type(self.supervisor_name_input, supervisor_name)

    def click_search_button(self) -> None:
        self.click(self.search_button)

    def click_reset_button(self) -> None:
        self.click(self.reset_button)
