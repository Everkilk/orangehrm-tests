from core.base_page import BasePage


class AdminPage(BasePage):
    admin_menu = BasePage.by_xpath("//span[text()='Admin']")
    admin_header = BasePage.by_xpath("//h6[text()='Admin']")
    username_input = BasePage.by_xpath("(//input[contains(@class,'oxd-input')])[2]")
    search_button = BasePage.by_xpath("(//button[contains(@class,'oxd-button--medium')])[2]")
    reset_button = BasePage.by_xpath("(//button[contains(@class,'oxd-button--medium')])[1]")
    add_button = BasePage.by_xpath("(//button[contains(@class,'oxd-button--medium')])[3]")
    user_role_dropdown = BasePage.by_xpath("(//div[text()='-- Select --'])[1]")
    employee_name_input = BasePage.by_xpath("//label[text()='Employee Name']/following-sibling::div//input")
    status_dropdown = BasePage.by_xpath("(//div[text()='-- Select --'])[2]")
    add_username_input = BasePage.by_xpath("//label[text()='Username']/following-sibling::div//input")
    add_password_input = BasePage.by_xpath("//label[text()='Password']/following-sibling::div//input[@type='password']")
    add_confirm_password_input = BasePage.by_xpath("//label[text()='Confirm Password']/following-sibling::div//input[@type='password']")
    save_button = BasePage.by_xpath("//button[text()='Save']")

    system_user_role_dropdown = BasePage.by_xpath("(//div[@class='oxd-select-text-input'])[1]")
    system_employee_name_input = BasePage.by_xpath("//input[@placeholder='Type for hints...']")
    system_status_dropdown = BasePage.by_xpath("(//div[@class='oxd-select-text-input'])[2]")

    def open_module(self) -> None:
        self.click(self.admin_menu)

    def is_loaded(self) -> bool:
        return self.is_visible(self.admin_header)

    def search_by_username(self, username: str) -> None:
        self.type(self.username_input, username)
        self.click(self.search_button)

    def reset_filters(self) -> None:
        self.click(self.reset_button)

    def click_the_admin_menu(self) -> None:
        self.click(self.admin_menu)

    def enter_username_for_system_user(self, username: str) -> None:
        self.clear_and_type(self.username_input, username)

    def select_user_role_for_system_user(self, user_role: str) -> None:
        self.click(self.system_user_role_dropdown)
        self.click_xpath_text("span", user_role)

    def enter_employee_name_for_system_user(self, employee_name: str) -> None:
        self.clear_and_type(self.system_employee_name_input, employee_name)

    def select_status_for_system_user(self, status: str) -> None:
        self.click(self.system_status_dropdown)
        self.click_xpath_text("span", status)

    def click_reset_button_for_system_user(self) -> None:
        self.click(self.reset_button)

    def click_search_button_for_system_user(self) -> None:
        self.click(self.search_button)

    def click_add_button_for_system_user(self) -> None:
        self.click(self.add_button)

    def select_user_role(self, user_role: str) -> None:
        self.click(self.user_role_dropdown)
        self.click_xpath_text("span", user_role)

    def enter_employee_name(self, employee_name: str) -> None:
        self.clear_and_type(self.employee_name_input, employee_name)

    def select_status(self, status: str) -> None:
        self.click(self.status_dropdown)
        self.click_xpath_text("span", status)

    def enter_username(self, username: str) -> None:
        self.clear_and_type(self.add_username_input, username)

    def enter_password(self, password: str) -> None:
        self.clear_and_type(self.add_password_input, password)

    def enter_confirm_password(self, confirm_password: str) -> None:
        self.clear_and_type(self.add_confirm_password_input, confirm_password)

    def click_save_button(self) -> None:
        self.click(self.save_button)
