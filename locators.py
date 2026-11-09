from selenium.webdriver.common.by import By
import random

# Общие
HEADER_PROFILE_LINK = (By.CSS_SELECTOR, '[href="/account"]')
HEADER_CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']/p[contains(text(), 'Конструктор')]")
HEADER_ORDERS_LINK = (By.CSS_SELECTOR, '[href="/feed"]')
MODAL_WINDOW = (By.CLASS_NAME, 'Modal_modal_opened__3ISw4')
MODAL_CLOSE_BTN = (By.XPATH, ".//button[contains(@class,'Modal_modal__close_modified__3V5XS')]")

# Восстановление пароля
PASSWORD_RECOVERY_LINK = (By.CSS_SELECTOR, '[href="/forgot-password"]')
EMAIL_INPUT = (By.NAME, "name")
RECOVERY_BTN = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')] | //button[contains(text(), 'Восстановить')]")
SHOW_HIDE_PASSWORD_BTN = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*")
PASSWORD_FIELD = (By.NAME, "Пароль")
INPUT_NEW_PASS = (By.XPATH, "//input[@name = 'Введите новый пароль']/parent::div")
SUBMIT_LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]")
PASSWORD_PH = (By.XPATH, '//label[contains(text(),"Пароль")]')

# Личный кабинет / История заказов
ORDERS_HISTORY = (By.CSS_SELECTOR, '[href="/account/order-history"]')
ORDER_CARD = (By.XPATH, "//*[@class = 'OrderHistory_listItem__2x95r mb-6'][1]")
LOGOUT_BTN = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3')] | //button[contains(text(), 'Выход')]")

# Конструктор / Лента заказов
BASKET_LINK = (By.CLASS_NAME, "BurgerConstructor_basket__29Cd7")
INGREDIENT_ITEM = (By.XPATH, f"//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')][{random.randint(3, 9)}]")
COUNTER_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")
COUNTER_TOTAL = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")
ORDER_BUTTON = (By.XPATH, "//button[@data-testid='order-button'] | //*[normalize-space()='Оформить заказ']")
INGREDIENT_COUNTER = (By.XPATH, ".//p[@class='counter_counter__num__3nue1']")
BUN_ITEM = (By.XPATH, "//img[@alt='Краторная булка N-200i']/parent::a")

# Модалка заказа
MODAL_ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
MODAL_ORDER = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")

# Лента заказов (детали заказа из ленты)
FEED_ORDER_CARD = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, 'text_type_digits-default')]")
ORDER_NUMBER_AT_WORK = (By.XPATH, "//p[contains(text(), 'В работе:')]/following-sibling::ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li")
ORDER_NUMBER_PH = (By.XPATH, "//p[contains(text(), 'В работе:')]/following-sibling::ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[not(contains(text(), 'Все текущие заказы готовы!'))]")

