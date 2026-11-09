import allure
from pages.base_page import *
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import MAIN_URL


@allure.feature("Конструктор")
class MainPage(BasePage):

    @allure.step("Открываю главную страницу")
    def open(self):
        self.go_to(MAIN_URL)

    @allure.step("Перехожу по ссылке в шапке на '{url}'")
    def go_to_page(self, url, locator):
        return self.get_url_and_click(url, locator)

    @allure.step("Ищу корзину конструктора")
    def _get_basket(self):
        return self.wait.until(EC.visibility_of_element_located(BASKET_LINK))

    @allure.step("Добавляю булку в конструктор")
    def add_bun_once(self):
        basket = self._get_basket()
        bun = self.wait.until(EC.visibility_of_element_located(BUN_ITEM))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", bun
        )
        self.js_drag_and_drop(bun, basket)

    @allure.step("Добавляю ингредиент в конструктор")
    def add_ingredient_to_burger(self, locator):
        basket = self._get_basket()
        ingredient = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", ingredient
        )
        self.js_drag_and_drop(ingredient, basket)

    @allure.step("Читаю счётчик ингредиента")
    def get_ingredient_counter(self, locator):
        counter_el = self.wait.until(EC.visibility_of_element_located(locator))
        return counter_el.find_element(*INGREDIENT_COUNTER).text


    @allure.step("Открываю модальное окно с деталями ингредиента")
    def open_ingredient_modal(self):
        self.click_to_element(INGREDIENT_ITEM)
        return self.is_visible(MODAL_WINDOW)

    @allure.step("Закрываю модальное окно")
    def close_modal(self):
        try:
            self.click_to_element(MODAL_CLOSE_BTN)
            self.wait_modal_invisible(MODAL_WINDOW)
        except TimeoutException:
            pass

    @allure.step("Проверяю закрытие модального окна")
    def modal_is_closed(self):
        """Истина, если модального окна нет в DOM"""
        return not self.driver.find_elements(*MODAL_WINDOW)

    @allure.step("Оформляю заказ")
    def place_order(self):
        self.click_to_element(ORDER_BUTTON)
        self.wait.until(EC.visibility_of_element_located(MODAL_ORDER_NUMBER))

    @allure.step("Получаю номер заказа")
    def order_number(self):
        def number_ready(d):
            el = d.find_element(*MODAL_ORDER_NUMBER)
            text = el.text.strip()
            return el if text.isdigit() and text != "9999" else False
        return self.wait.until(number_ready).text.strip()