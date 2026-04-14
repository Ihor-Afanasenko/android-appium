from enum import Enum


class Capabilities(Enum):
    JOOM_ANDROID_CHROME = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "platformVersion": "17",
        "browserName": "Chrome",
        "deviceName": "Pixel 9 Pro",
        "chromedriverExecutable": "/home/ihor/PycharmProjects/appium_examples-master/app/chromedriver",
        "autoGrantPermissions": True,
    }

    JOOM_ANDROID_APP = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "platformVersion": "17",
        "deviceName": "Pixel 9 Pro",
        "appium:autoGrantPermissions": True,
        "app": "/home/ihor/PycharmProjects/android_appium/app/joom_4.182.0.apk",
    }
