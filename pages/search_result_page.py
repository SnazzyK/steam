from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class SearchPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.old_list = []

    # Locators
    TIMEOUT_10 = 10
    BUTTON_SORT = (By.XPATH, "//*[@id='sort_by_dselect_container']")
    PRICE_DESC = (By.XPATH, "//*[@id='Price_DESC']")
    ITEMS = (By.XPATH, "//a[@data-gpnav='item']")

    # Getters
    def get_button_sort(self):
        return WebDriverWait(self.driver, self.TIMEOUT_10).until(
            EC.visibility_of_element_located(self.BUTTON_SORT))

    def get_price_desc(self):
        return WebDriverWait(self.driver, self.TIMEOUT_10).until(
            EC.visibility_of_element_located(self.PRICE_DESC))

    def get_list_items(self, value):
        all_list = WebDriverWait(self.driver, self.TIMEOUT_10).until(
            EC.visibility_of_all_elements_located(self.ITEMS))
        return [item for item in all_list[:value]]

    def wait_for_list_update(self, old_list):
        WebDriverWait(self.driver, self.TIMEOUT_10).until(
            lambda d: [item.text for item in d.find_elements(*self.ITEMS)] != old_list
        )

    # Action
    def click_button_sort(self):
        self.get_button_sort().click()

    def click_price_desc(self):
        self.get_price_desc().click()

    def take_lists_items(self, value):
        list_elements = self.get_list_items(value)
        for item in list_elements:
            print(item.text)

    def sort(self, value):
        self.old_list = [item.text for item in self.get_list_items(value)]

    # Methods
    def sort_price_desc(self, value):
        self.sort(value)
        self.click_button_sort()
        self.click_price_desc()
        self.wait_for_list_update(self.old_list)
        self.take_lists_items(value)
