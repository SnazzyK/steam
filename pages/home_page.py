from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class HomePage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    SEARCH_FIELDS = (By.XPATH, "//input[@id = 'store_nav_search_term']")
    TIMEOUT_10 = 10
    BUTTON_SEARCH = (By.XPATH, "//*[@id = 'store_search_link']//img")

    # Getters
    def get_search_fields(self):
        return WebDriverWait(self.driver, self.TIMEOUT_10).until(
            EC.visibility_of_element_located(self.SEARCH_FIELDS))

    def get_button_search(self):
        return WebDriverWait(self.driver, self.TIMEOUT_10).until(
            EC.visibility_of_element_located(self.BUTTON_SEARCH))

    # Action
    def input_search_fields(self, name):
        self.get_search_fields().send_keys(name)

    def click_button_search(self):
        self.get_button_search().click()

    # Methods
    def search(self, name):
        self.input_search_fields(name)
        self.click_button_search()
