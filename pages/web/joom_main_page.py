from appium import webdriver
from appium.webdriver.common.appiumby import (
    AppiumBy,
)
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
)

from pages.joom_abstract import JoomAbstract


class JoomMainPage(JoomAbstract):
    def close_initial_dialog(self):
        try:
            self.modal_close_button.click()
        except NoSuchElementException:
            pass

        return self

    def get_item_prices(self):
        pass

    def get_found_items(self):
        pass

    def select_search_suggestion(self, index):
        return self

    def __init__(self, driver: webdriver.Remote):
        super().__init__(driver)
        self.driver.get("https://www.joom.com/en")

    @property
    def modal_close_button(self):
        return self.driver.find_element(
            AppiumBy.CSS_SELECTOR,
            "[aria-label=Close]",
        )

    @property
    def search_field(self):
        return self.driver.find_element(AppiumBy.TAG_NAME, "form")

    def _insert_search_item(self, item):
        self.action.click(self.search_field).perform()
        self.action.send_keys(item)

    def enter_search_item(self, item: str):
        try:
            self._insert_search_item(item)
        except ElementNotInteractableException:
            web_view = self.driver.context
            self.driver.switch_to.context("NATIVE_APP")
            self.driver.find_element(
                AppiumBy.XPATH,
                ".//android.widget.Button[@text='Allow']",
            ).click()
            self.driver.switch_to.context(web_view)
            self._insert_search_item(item)

        return self
