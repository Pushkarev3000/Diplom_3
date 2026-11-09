import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators import *
from urls import *


@allure.feature("Личный кабинет")
class ProfilePage(BasePage):
    """Личный кабинет пользователя"""

    @allure.step("Открываю профиль через кнопку «Личный кабинет» в шапке")
    def go_to_profile(self):
        self.get_url_and_click(MAIN_URL, HEADER_PROFILE_LINK)
        self.wait_until_url_contains("/profile")

    @allure.step("Перехожу в раздел «История заказов»")
    def go_to_history(self):
        self.click_to_element(ORDERS_HISTORY)
        self.wait_until_url_contains(HISTORY_ORDERS_URL)

    @allure.step("Выхожу из аккаунта")
    def logout(self):
        self.click_to_element(LOGOUT_BTN)
        self.wait_until_url_contains(LOGIN_URL)

    @allure.step("Проверяю, что пользователь авторизован")
    def is_logged_in(self):
        try:
            self.wait_until_clickable(PASSWORD_PH)
        except TimeoutException:
            return False
        return len(self.driver.find_elements(*LOGOUT_BTN)) > 0