#почему-то allure отчет не хотел работать без кода ниже, не мог найти импортированные urls
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from helpers import *
from urls import *
from locators import *
from pages.main_page import *
from pages.feed_page import *
from pages.profile_page import *
from pages.recovery_page import *
import pytest
from driver_factory import DriverFactory

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to use: chrome or firefox",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = DriverFactory.get_driver(
        browser=browser,
        headless=headless,
    )
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 3)

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture
def feed_page(driver):
    page = FeedPage(driver)
    return page

@pytest.fixture
def profile_page(driver):
    page = ProfilePage(driver)
    return page

@pytest.fixture
def recovery_page(driver):
    page = RecoveryPage(driver)
    return page

@pytest.fixture
def auth_user(driver, wait):
    user_data = unique_user_data()
    user = registered_user(user_data)
    driver.get(LOGIN_URL)
    email_input = wait.until(EC.visibility_of_element_located(EMAIL_INPUT))
    email_input.clear()
    email_input.send_keys(user["email"])
    password_input = wait.until(EC.visibility_of_element_located(PASSWORD_FIELD))
    password_input.clear()
    password_input.send_keys(user["password"])
    btn = wait.until(EC.element_to_be_clickable(SUBMIT_LOGIN_BTN))
    try:
        btn.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", btn)
    wait.until(EC.visibility_of_element_located(ORDER_BUTTON))
    yield user, driver
    delete_user(user["token_header"])

@pytest.fixture
def create_new_order(auth_user, main_page, wait):
    def _create_order():
        main_page.add_bun_once()
        main_page.add_ingredient_to_burger(INGREDIENT_ITEM)
        main_page.place_order()
        order_number = main_page.order_number()
        cross = wait.until(EC.element_to_be_clickable(MODAL_CLOSE_BTN))
        try:
            cross.click()
        except ElementClickInterceptedException:
            main_page.driver.execute_script("arguments[0].click();", cross)
        wait.until(EC.invisibility_of_element_located(MODAL_ORDER)
        )
        return order_number
    return _create_order
