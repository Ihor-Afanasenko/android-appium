from abc import ABC, abstractmethod

from appium import webdriver
from selenium.webdriver import ActionChains


class JoomAbstract(ABC):
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.action = ActionChains(self.driver)

    @abstractmethod
    def close_initial_dialog(self):
        raise NotImplementedError("Abstract method. Please rewrite in the derived class")

    @abstractmethod
    def close_wheel_of_fortune_dialog(self):
        raise NotImplementedError("Abstract method. Please rewrite in the derived class")

    @abstractmethod
    def enter_search_item(self, item: str):
        raise NotImplementedError("Abstract method. Please rewrite in the derived class")

    @abstractmethod
    def select_search_suggestion(self, index):
        raise NotImplementedError("Abstract method. Please rewrite in the derived class")

    @abstractmethod
    def get_found_items(self):
        raise NotImplementedError("Abstract method. Please rewrite in the derived class")

    @abstractmethod
    def get_item_prices(self):
        raise NotImplementedError()

    @abstractmethod
    def click_shopping_cart(self):
        raise NotImplementedError()

    @abstractmethod
    def click_favourites(self):
        raise NotImplementedError()

    @abstractmethod
    def click_back_button(self):
        raise NotImplementedError()

    @abstractmethod
    def get_toolbar_title(self):
        raise NotImplementedError()

    @abstractmethod
    def is_search_bar_displayed(self):
        raise NotImplementedError()
