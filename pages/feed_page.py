import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from urls import *


@allure.feature("Лента заказов")
class FeedPage(BasePage):
    """Раздел «Лента заказов»"""

    @allure.step("Открываю ленту заказов")
    def open_feed(self):
        self.go_to(FEED_URL)

    @allure.step("Перехожу в «Историю заказов» через личный кабинет")
    def go_to_history(self):
        self.click_to_element(HEADER_PROFILE_LINK)
        self.click_to_element(ORDERS_HISTORY)
        self.wait_until_url_contains(HISTORY_ORDERS_URL)

    @allure.step("Возвращаюсь в ленту по кнопке в шапке")
    def go_to_feed_from_header(self):
        self.click_to_element(HEADER_ORDERS_LINK)
        self.wait_until_url_contains(FEED_URL)

    @allure.step("Читаю номер заказа из раздела «В работе»")
    def get_order_in_work(self):
        long_wait = WebDriverWait(self.driver, 15)
        long_wait.until(EC.presence_of_element_located(ORDER_NUMBER_PH))
        return self.find_element_ext(ORDER_NUMBER_AT_WORK).text

    @allure.step("Собираю номера заказов, видимых на странице")
    def get_visible_order_numbers(self):
        self.driver.implicitly_wait(10)
        self.wait.until(EC.presence_of_element_located(ORDER_CARD))
        items = self.driver.find_elements(*ORDER_NUMBER)
        return [el.text.strip() for el in items if el.text.strip()]

    @allure.step("Открываю карточку заказа — модалку с деталями")
    def open_order_modal(self):
        self.wait.until(EC.presence_of_element_located(ORDER_NUMBER))
        self.click_to_element(ORDER_NUMBER)
        return self.is_visible(MODAL_WINDOW)

    @allure.step("Читаю счётчики выполненных заказов")
    def get_counters(self):
        total = int(self.find_element_ext(COUNTER_TOTAL).text)
        today = int(self.find_element_ext(COUNTER_TODAY).text)
        return total, today
