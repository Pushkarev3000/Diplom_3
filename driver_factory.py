from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:

    @staticmethod
    def get_driver(browser: str, headless: bool):
        if browser == "chrome":
            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

            options.set_preference("ui.prefersReducedMotion", 1)
            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        return driver