import allure

@allure.feature("Восстановление пароля")
class TestRecoveryPage:

    @allure.title("Переход на страницу восстановления по кнопке «Восстановить пароль»")
    def test_navigate_to_recovery_page(self, recovery_page):
        recovery_page.open_recovery_from_login()
        assert "/forgot-password" in recovery_page.get_current_url(), \
            f"Не перешли на страницу восстановления, URL: {recovery_page.get_current_url()}"

    @allure.title("Ввод почты и клик по кнопке «Восстановить» отправляет форму")
    def test_recover_with_email_submits_form(self, recovery_page):
        recovery_page.open_recovery_from_login()
        recovery_page.submit_email('testTest777@ya.ru')
        recovery_page.wait_left_recovery_page()
        assert "/forgot-password" not in recovery_page.get_current_url(), \
            "После клика «Восстановить» не произошёл переход"

    @allure.title("Кнопка показать/скрыть делает поле пароля активным")
    def test_show_hide_password_activates_field(self, recovery_page):
        recovery_page.open_recovery_from_login()
        recovery_page.submit_email('testTest777@ya.ru')
        recovery_page.toggle_show_password()
        recovery_page.wait_active_password_border()
        colors = recovery_page.get_password_border_colors()
        assert colors, "Поле пароля не найдено на странице"          # ← фикс мимо-прохода
        assert all(c == "rgb(76, 76, 255)" for c in colors), \
            f"Рамка поля не активна: {colors}"

