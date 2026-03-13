from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import EXPLICIT_WAIT_SECONDS


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT_SECONDS)

    def visit(self, url: str) -> None:
        self.driver.get(url)

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_xpath_text(self, tag: str, text_value: str) -> None:
        locator = (By.XPATH, f"//{tag}[normalize-space(text())='{text_value}']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: tuple[str, str], value: str) -> None:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def clear_and_type(self, locator: tuple[str, str], value: str) -> None:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def text(self, locator: tuple[str, str]) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except Exception:
            return False

    def current_url(self) -> str:
        return self.driver.current_url

    def find_all(self, locator: tuple[str, str]):
        return self.driver.find_elements(*locator)

    def wait_url_contains(self, value: str) -> None:
        self.wait.until(EC.url_contains(value))

    def back(self) -> None:
        self.driver.back()

    @staticmethod
    def by_xpath(value: str) -> tuple[str, str]:
        return (By.XPATH, value)

    @staticmethod
    def by_css(value: str) -> tuple[str, str]:
        return (By.CSS_SELECTOR, value)

    @staticmethod
    def by_name(value: str) -> tuple[str, str]:
        return (By.NAME, value)
