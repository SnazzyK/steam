from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_driver()
        return cls._instance

    def _initialize_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def get_driver(cls):
        if cls._instance is None:
            cls()
        return cls._instance.driver

    @classmethod
    def quit_driver(cls):
        if cls._instance and cls._instance.driver:
            cls._instance.driver.quit()
            cls._instance = None
