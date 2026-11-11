from pages.base_page import BasePage
from locators import *
from urls import *


class RecoveryPage(BasePage):
    """Страница восстановления пароля"""

    def open_recovery_from_login(self):
        """С главной страницы логина перейти по ссылке «Восстановить пароль»"""
        self.go_to(LOGIN_URL)
        self.click_to_element(PASSWORD_RECOVERY_LINK)
        self.wait_until_url_contains(PASSWORD_RECOVERY_URL)

    def submit_email(self, email):
        """Ввести почту и нажать «Восстановить»"""
        self.input_text(EMAIL_INPUT, email)
        self.click_to_element(RECOVERY_BTN)

    def wait_left_recovery_page(self):
        """Дождаться ухода со страницы восстановления (форма отправилась)"""
        self.wait.until(lambda d: PASSWORD_RECOVERY_URL not in d.current_url)

    def toggle_show_password(self):
        """Клик по кнопке показать/скрыть пароль"""
        self.click_to_element(SHOW_HIDE_PASSWORD_BTN)

    def get_password_border_colors(self):
        """Список цветов рамок полей пароля"""
        fields = self.find_elements_ext(INPUT_NEW_PASS)
        return [el.value_of_css_property("border-color") for el in fields]

    def wait_active_password_border(self, color="rgb(76, 76, 255)"):
        def active(d):
            els = d.find_elements(*INPUT_NEW_PASS)
            return any(el.value_of_css_property("border-color") == color for el in els) \
                if els else False
        self.wait.until(active)
