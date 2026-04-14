import pytest

from conf.capabilities import Capabilities
from helper.browser import get_browser


@pytest.fixture
def main_page(request):
    mode = request.config.getoption("--app_type")

    if mode == "web":
        from pages.web.joom_main_page import (
            JoomMainPage,
        )

        pg = JoomMainPage(get_browser(Capabilities.JOOM_ANDROID_CHROME.value))
        yield pg
        pg.driver.quit()

    elif mode == "native":
        from pages.native.joom_main_page import (
            JoomMainPage,
        )

        pg = JoomMainPage(get_browser(Capabilities.JOOM_ANDROID_APP.value))
        yield pg
        pg.driver.quit()

    else:
        raise AssertionError("Incorrect mode. Can be web or native")
