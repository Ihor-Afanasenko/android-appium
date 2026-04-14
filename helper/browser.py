from appium import webdriver
from appium.options.common import AppiumOptions


def get_browser(caps: dict) -> webdriver.Remote:
    return webdriver.Remote(
        "http://localhost:4723",
        options=AppiumOptions().load_capabilities(caps),
    )
