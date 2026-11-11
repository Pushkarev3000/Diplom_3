import allure
from urls import *
from locators import *

@allure.feature("Личный кабинет")
class TestProfilePage:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_click_profile_navigates_to_profile_page(self, auth_user, profile_page):
        profile_page.go_to_profile()
        assert profile_page.get_current_url().endswith("/profile"), \
            "Не перешли на страницу профиля"

    @allure.title("Переход в раздел «История заказов» из Личного кабинета")
    def test_history_orders_tab_opens_history_section(self, create_new_order, profile_page):
        create_new_order()
        profile_page.go_to_profile()
        profile_page.go_to_history()
        assert profile_page.get_current_url().endswith("/account/order-history"), \
            "Не перешли на страницу истории заказов"

    @allure.title("Выход из аккаунта возвращает на страницу входа")
    def test_logout_redirects_to_login_page(self, auth_user, profile_page):
        profile_page.go_to_profile()
        assert profile_page.is_logged_in(), "Пользователь не авторизован до выхода"
        profile_page.logout()
        assert not profile_page.is_logged_in(), "Индикатор пользователя остался после выхода"
        assert "/login" in profile_page.get_current_url(), \
            "После выхода не попали на страницу входа"