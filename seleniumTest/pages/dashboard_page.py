from core.base_page import BasePage


class DashboardPage(BasePage):
    dashboard_header = BasePage.by_xpath("//h6[text()='Dashboard']")
    quick_launch_cards = BasePage.by_css(".orangehrm-quick-launch-card")
    side_menu_items = BasePage.by_css(".oxd-main-menu-item")
    clock_icon = BasePage.by_xpath("//i[contains(@class,'bi-stopwatch')]")
    my_actions_notification = BasePage.by_xpath("//button[contains(@class,'oxd-icon-button--danger')]/following-sibling::p[1]")
    assign_leave = BasePage.by_xpath("//*[@title='Assign Leave']")
    leave_list = BasePage.by_xpath("//*[@title='Leave List']")
    timesheets = BasePage.by_xpath("//*[@title='Timesheets']")
    apply_leave = BasePage.by_xpath("//*[@title='Apply Leave']")
    my_leave = BasePage.by_xpath("//*[@title='My Leave']")
    my_timesheet = BasePage.by_xpath("//*[@title='My Timesheet']")
    buzz_card = BasePage.by_xpath("(//div[@class='orangehrm-buzz-profile-image']//img)[1]")
    settings_icon = BasePage.by_xpath("//i[contains(@class,'bi-gear-fill')]")
    employee_leave_close = BasePage.by_xpath("//button[contains(@class,'oxd-dialog-close-button')]")
    employee_leave_cancel = BasePage.by_xpath("(//button[contains(@class,'oxd-button--medium')])[1]")
    employee_leave_save = BasePage.by_xpath("(//button[contains(@class,'oxd-button--medium')])[2]")
    employee_leave_checkbox = BasePage.by_xpath("//span[contains(@class,'oxd-switch-input')]")
    engineering = BasePage.by_xpath("//span[@title='Engineering']")
    human_resources = BasePage.by_xpath("//span[@title='Human Resources']")
    unassigned = BasePage.by_xpath("(//span[@title='Unassigned'])[2]")
    admin_menu = BasePage.by_xpath("(//a[@class='oxd-main-menu-item']//span)[1]")

    def is_loaded(self) -> bool:
        return self.is_visible(self.dashboard_header)

    def quick_launch_count(self) -> int:
        return len(self.find_all(self.quick_launch_cards))

    def side_menu_count(self) -> int:
        return len(self.find_all(self.side_menu_items))

    def name_of_page(self) -> str:
        return self.text(self.dashboard_header)

    def clock_icon_click(self) -> str:
        self.click(self.clock_icon)
        return self.current_url()

    def my_notification(self) -> str:
        self.click(self.my_actions_notification)
        return self.current_url()

    def assign_leave_click(self) -> str:
        self.click(self.assign_leave)
        return self.driver.title

    def leave_list_click(self) -> str:
        self.click(self.leave_list)
        return self.current_url()

    def timesheet_click(self) -> str:
        self.click(self.timesheets)
        return self.current_url()

    def apply_leave_click(self) -> str:
        self.click(self.apply_leave)
        return self.current_url()

    def my_leave_click(self) -> str:
        self.click(self.my_leave)
        return self.current_url()

    def my_timesheet_click(self) -> str:
        self.click(self.my_timesheet)
        return self.current_url()

    def employee_leave_setting_icon(self) -> None:
        self.click(self.settings_icon)

    def employee_leave_close_click(self) -> None:
        self.click(self.employee_leave_close)

    def employee_leave_cancel_click(self) -> None:
        self.click(self.employee_leave_cancel)

    def employee_leave_checkbox_click(self) -> None:
        self.click(self.employee_leave_checkbox)

    def employee_leave_save_click(self) -> None:
        self.click(self.employee_leave_save)

    def buzz_page(self) -> str:
        self.click(self.buzz_card)
        return self.current_url()

    def engineering_click(self) -> None:
        self.click(self.engineering)

    def human_resource_click(self) -> None:
        self.click(self.human_resources)

    def unassigned_click(self) -> None:
        self.click(self.unassigned)

    def admin_menu_verify(self) -> str:
        self.click(self.admin_menu)
        return self.current_url()

    def scroll_page(self) -> None:
        self.driver.execute_script("window.scrollBy(300, 500);")
