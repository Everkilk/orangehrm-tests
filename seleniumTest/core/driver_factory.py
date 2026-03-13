from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.settings import HEADLESS, WINDOW_SIZE


def create_driver() -> webdriver.Chrome:
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument(f"--window-size={WINDOW_SIZE}")
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
