from time import sleep

from appium.webdriver.common.appiumby import (
    AppiumBy,
)
from appium.webdriver.extensions.android.nativekey import (
    AndroidKey,
)
from selenium.common.exceptions import (
    NoSuchElementException,
)

from pages.joom_abstract import JoomAbstract


class JoomMainPage(JoomAbstract):
    @property
    def initial_dialog_swiper(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Close")

    @property
    def search_field_unfocused(self):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Search on Joom")',
        )

    @property
    def search_field_focused(self):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.joom:id/input")',
        )

    @property
    def shopping_cart(self):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Shopping cart")',
        )

    @property
    def favorites_menu(self):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Favourites")',
        )

    @property
    def back_button(self):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.joom:id/toolbar_navigation_button")',
        )

    @property
    def search_suggestions(self):
        return self.driver.find_elements(
            AppiumBy.XPATH,
            "//android.widget.Button",
        )

    def close_initial_dialog(self):
        try:
            self.initial_dialog_swiper.click()
        except NoSuchElementException:
            pass
        return self

    def close_wheel_of_fortune_dialog(self):
        try:
            self.initial_dialog_swiper.click()
        except NoSuchElementException:
            pass
        return self

    def enter_search_item(self, item: str):
        self.search_field_unfocused.click()
        self.search_field_unfocused.click()
        self.action.send_keys_to_element(self.search_field_unfocused, item).perform()
        self.driver.hide_keyboard()
        self.action.send_keys(item).perform()
        sleep(5)
        return self

    def select_search_suggestion(self, index):
        self.search_suggestions[index].click()
        return self

    def click_shopping_cart(self):
        self.shopping_cart.click()
        return self

    def click_favourites(self):
        self.favorites_menu.click()
        return self

    def click_back_button(self):
        self.back_button.click()
        return self

    def start_search(self):
        self.driver.press_keycode(AndroidKey.TAB).press_keycode(AndroidKey.SEARCH)

    def get_found_items(self):
        return self.driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.joom:id/product_view")',
        )

    def get_toolbar_title(self):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.joom:id/toolbar_title")',
        ).text

    def is_search_bar_displayed(self):
        return self.search_field_unfocused.is_displayed()

    def get_item_prices(self):
        return self.driver.find_elements(
            AppiumBy.XPATH,
            '//*[contains(@content-desc, "UAH")]',
        )
