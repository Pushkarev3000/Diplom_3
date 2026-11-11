import allure
from urls import *
from locators import *


@allure.feature("Главная страница — конструктор")
class TestMainPage:

    @allure.title("Переход по клику на «Лента заказов»")
    def test_header_orders_nav(self, main_page):
        main_page.go_to_page(MAIN_URL, HEADER_ORDERS_LINK)
        assert main_page.get_current_url() == FEED_URL, \
            "Неверный URL после перехода в Ленту заказов"
        assert main_page.is_visible(FEED_ORDER_CARD), \
            "Карточки заказов не отображаются в ленте"

    @allure.title("Переход по клику на «Конструктор»")
    def test_header_constructor_nav(self, main_page):
        main_page.go_to_page(FEED_URL, HEADER_CONSTRUCTOR_LINK)
        assert main_page.get_current_url() == MAIN_URL, \
            "Неверный URL после перехода в Конструктор"
        assert main_page.is_visible(BASKET_LINK), \
            "Корзина конструктора не отображается"

    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_ingredient_modal_opens(self, main_page):
        main_page.go_to(MAIN_URL)
        modal = main_page.open_ingredient_modal()
        assert modal.is_displayed(), "Модальное окно не отображается"

    @allure.title("Окно с деталями закрывается кликом по крестику")
    def test_modal_close_by_cross(self, main_page):
        main_page.go_to(MAIN_URL)
        main_page.open_ingredient_modal()
        main_page.close_modal()
        assert main_page.modal_is_closed(), "Модальное окно всё ещё открыто"

    @allure.title("Счётчик булки после добавления в конструктор равен 2")
    def test_constructor_bun_counter(self, main_page, auth_user):
        main_page.go_to(MAIN_URL)
        main_page.add_bun_once()
        after_bun_count = main_page.get_ingredient_counter(BUN_ITEM)
        assert after_bun_count == '2', (
            f"Счётчик не увеличился после добавления булки: стало {after_bun_count}"
        )

    @allure.title("Счётчик ингредиента увеличивается на 1 при добавлении")
    def test_constructor_ingredient_counter(self, main_page, auth_user):
        main_page.go_to(MAIN_URL)
        main_page.add_bun_once()
        item = INGREDIENT_ITEM
        count_before = main_page.get_ingredient_counter(item)
        main_page.add_ingredient_to_burger(item)
        count_after = main_page.get_ingredient_counter(item)
        assert int(count_after) - int(count_before) == 1, (
            f"Счётчик не обновился после добавления ингредиента: стало {count_after}"
        )

    @allure.title("После оформления заказа отображается его номер")
    def test_order_number(self, main_page, auth_user):
        main_page.go_to(MAIN_URL)
        main_page.add_bun_once()
        main_page.add_ingredient_to_burger(INGREDIENT_ITEM)
        main_page.place_order()
        order_number = main_page.order_number()
        assert order_number.isdigit(), (
            f"Не получен корректный номер заказа: {order_number}"
        )