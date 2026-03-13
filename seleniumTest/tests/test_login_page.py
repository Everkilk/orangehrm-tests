import pytest
from urllib.request import Request, urlopen

from pages.login_page import LoginPage


class TestLoginPage:
    login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    def _validate_broken_links(self, driver) -> None:
        links = driver.find_elements("tag name", "a")
        for link in links:
            href = link.get_attribute("href")
            if not href or not href.startswith("http"):
                continue
            try:
                req = Request(href, method="HEAD")
                with urlopen(req, timeout=5):
                    pass
            except Exception:
                continue

    @pytest.fixture
    def page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        return login_page

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_with_empty_username(self, page):
        page.login_credential("", "123")
        page.wait_url_contains("auth/login")
        assert page.current_url() == self.login_url

    @pytest.mark.regression
    def test_login_with_invalid_email(self, page):
        page.login_credential("baskar@gmail.com", "123")
        page.wait_url_contains("auth/login")
        assert page.current_url() == self.login_url

    @pytest.mark.regression
    def test_login_with_empty_credentials(self, page):
        page.login_credential("", "")
        page.wait_url_contains("auth/login")
        assert page.current_url() == self.login_url

    @pytest.mark.regression
    def test_login_with_invalid_password(self, page):
        page.login_credential("Admin", "123")
        page.wait_url_contains("auth/login")
        assert page.current_url() == self.login_url

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_with_valid_credentials(self, page):
        page.login_credential("Admin", "admin123")
        page.wait_url_contains("dashboard")
        assert page.current_url() == self.dashboard_url

    @pytest.mark.regression
    def test_forgot_password_navigation(self, page):
        page.click_forgot_password_link()
        page.wait_url_contains("requestPasswordResetCode")
        assert page.current_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"

    @pytest.mark.regression
    def test_cancel_forgot_password(self, page):
        page.click_forgot_password_link()
        page.cancel_password_reset()
        page.wait_url_contains("auth/login")
        assert page.current_url() != "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"

    @pytest.mark.regression
    def test_reset_password_flow(self, page):
        page.click_forgot_password_link()
        page.reset_password("Admin")
        page.wait_url_contains("sendPasswordReset")
        assert page.current_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"

    @pytest.mark.smoke
    def test_logo_visibility(self, page):
        assert page.logo_visible()
        assert page.side_logo_visible()

    @pytest.mark.regression
    def test_page_title_text(self, page):
        assert page.title_text().strip().lower() == "login"

    @pytest.mark.regression
    def test_page_title_visibility(self, page):
        assert page.page_title_visible()

    @pytest.mark.regression
    def test_social_icon_linkedin(self, page):
        assert page.linkedin_icon_visible()

    @pytest.mark.regression
    def test_social_icon_facebook(self, page):
        assert page.facebook_icon_visible()

    @pytest.mark.regression
    def test_social_icon_twitter(self, page):
        assert page.twitter_icon_visible()

    @pytest.mark.regression
    def test_social_icon_youtube(self, page):
        assert page.youtube_icon_visible()

    @pytest.mark.regression
    def test_invalid_user_login_from_dataprovider_equivalent(self, page):
        page.login_credential("Karthik", "B")
        page.wait_url_contains("auth/login")
        assert page.current_url() != self.dashboard_url

    @pytest.mark.regression
    def test_check_broken_links(self, page):
        self._validate_broken_links(page.driver)
