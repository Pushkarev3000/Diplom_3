import allure
from selenium.webdriver.support import expected_conditions as EC
from urls import *
from locators import *


@allure.feature("Лента заказов")
class TestFeedPage:
    """Тесты раздела «Лента заказов»"""

    @allure.title("Новый заказ появляется в разделе «В работе»")
    def test_new_order_appears_in_work_in_progress(self, feed_page, create_new_order):
        order = create_new_order()
        feed_page.open_feed()
        work_order = feed_page.get_order_in_work()
        assert order in work_order, f"Номер заказа {order} не найден в «В работе»"

    @allure.title("Заказы из «Истории заказов» отображаются в ленте")
    def test_history_orders_displayed_in_feed(self, feed_page, create_new_order):
        order_1 = create_new_order()
        order_2 = create_new_order()
        feed_page.go_to_history()
        history_texts = feed_page.get_visible_order_numbers()
        print(f'ЛК ЗАКАЗЫ {history_texts}')
        feed_page.go_to_feed_from_header()
        feed_texts = feed_page.get_visible_order_numbers()
        print(f'ВСЕ ЗАКАЗЫ {feed_texts}')
        assert history_texts, "История заказов пуста"
        assert all(el in feed_texts for el in history_texts), \
            "В ленте нет заказов из «Истории заказов»"

    @allure.title("Клик по заказу открывает модальное окно с деталями")
    def test_click_order_opens_modal(self, feed_page):
        feed_page.open_feed()
        modal = feed_page.open_order_modal()
        assert modal.is_displayed()

    @allure.title("Счётчики выполненных заказов увеличиваются после нового заказа")
    def test_counters_increase_after_new_order(self, feed_page, create_new_order):
        feed_page.open_feed()
        total_before, today_before = feed_page.get_counters()
        feed_page.go_to(MAIN_URL)
        create_new_order()
        feed_page.open_feed()
        total_after, today_after = feed_page.get_counters()
        assert total_after > total_before, "Счётчик «Выполнено за всё время» не увеличился"
        assert today_after > today_before, "Счётчик «Выполнено за сегодня» не увеличился"