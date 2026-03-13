from core.base_page import BasePage
from config.settings import BASE_URL


class LoginPage(BasePage):
    username_input = BasePage.by_name("username")
    password_input = BasePage.by_name("password")
    login_button = BasePage.by_xpath("//button[@type='submit']")
    page_title = BasePage.by_xpath("//h5")
    error_message = BasePage.by_xpath("//p[contains(@class,'alert-content-text')]")
    logo = BasePage.by_xpath("//img[@alt='company-branding']")
    side_logo = BasePage.by_xpath("//div[@class='orangehrm-login-logo']")
    forgot_password_link = BasePage.by_xpath("//p[contains(.,'Forgot your password?')]")
    forgot_user = BasePage.by_name("username")
    cancel_button = BasePage.by_xpath("//*[text()=' Cancel ']")
    reset_password_button = BasePage.by_xpath("//*[text()=' Reset Password ']")
    linkedin_icon = BasePage.by_xpath("//a[contains(@href,'linkedin.com/company/orangehrm')]")
    facebook_icon = BasePage.by_xpath("//a[contains(@href,'facebook.com/OrangeHRM')]")
    twitter_icon = BasePage.by_xpath("//a[contains(@href,'twitter.com/orangehrm')]")
    youtube_icon = BasePage.by_xpath("//a[contains(@href,'youtube.com/c/OrangeHRMInc')]")

    def open(self) -> None:
        self.visit(f"{BASE_URL}/auth/login")

    def login(self, username: str, password: str) -> None:
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

    def login_credential(self, username: str, password: str) -> None:
        self.login(username, password)

    def click_forgot_password_link(self) -> None:
        self.click(self.forgot_password_link)

    def cancel_password_reset(self) -> None:
        self.click(self.cancel_button)

    def reset_password(self, username: str) -> None:
        self.type(self.forgot_user, username)
        self.click(self.reset_password_button)

    def go_back(self) -> None:
        self.back()

    def title_text(self) -> str:
        return self.text(self.page_title)

    def logo_visible(self) -> bool:
        return self.is_visible(self.logo)

    def side_logo_visible(self) -> bool:
        return self.is_visible(self.side_logo)

    def page_title_visible(self) -> bool:
        return self.is_visible(self.page_title)

    def error_visible(self) -> bool:
        return self.is_visible(self.error_message)

    def on_dashboard(self) -> bool:
        return "dashboard" in self.current_url()

    def linkedin_icon_visible(self) -> bool:
        return self.is_visible(self.linkedin_icon)

    def facebook_icon_visible(self) -> bool:
        return self.is_visible(self.facebook_icon)

    def twitter_icon_visible(self) -> bool:
        return self.is_visible(self.twitter_icon)

    def youtube_icon_visible(self) -> bool:
        return self.is_visible(self.youtube_icon)
