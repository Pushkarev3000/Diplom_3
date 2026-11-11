from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver, timeout=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element_ext(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)

    def input_text(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def get_current_url(self):
        return str(self.driver.current_url)

    def go_to(self, url: str):
        """Открыть URL и дождаться загрузки (хотя бы body)"""
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def get_url_and_click(self, url, locator):
        self.go_to(url)
        self.click_to_element(locator)

    def is_visible(self, locator):
        """Ждать, пока модалка появится"""
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    def wait_modal_invisible(self, modal_locator):
        """Ждать, пока модалка исчезнет"""
        self.wait.until(EC.invisibility_of_element_located(modal_locator))

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_url_contains(self, substring):
        return self.wait.until(lambda d: substring in d.current_url)

    def find_elements_ext(self, locator):
        """Ждать появления хотя бы одного элемента и вернуть список всех"""
        # self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def wait_ext(self, driver):
        return self.driver.implicitly_wait(10)

    def long_wait(self):
        return WebDriverWait(self.driver, 15)

    
    def scroll_to(self, element):
        """Прокрутить страницу к элементу"""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def js_drag_and_drop(self, source, target):
        """Эмуляция HTML5 drag-and-drop — работает в Firefox и Chrome."""
        self.driver.execute_script(
            """
            const [src, tgt] = arguments;
            const dt = new DataTransfer();

            src.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true, cancelable: true, dataTransfer: dt
            }));
            tgt.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true, cancelable: true, dataTransfer: dt
            }));
            tgt.dispatchEvent(new DragEvent('dragover', {
                bubbles: true, cancelable: true, dataTransfer: dt
            }));
            tgt.dispatchEvent(new DragEvent('drop', {
                bubbles: true, cancelable: true, dataTransfer: dt
            }));
            src.dispatchEvent(new DragEvent('dragend', {
                bubbles: true, cancelable: true, dataTransfer: dt
            }));
            """,
            source, target,
        )

