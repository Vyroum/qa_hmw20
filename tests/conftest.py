import os
import allure
import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser, support
from selene.support.shared import config
import config
import utils
from utils import file_location
from utils import allure_video


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    load_dotenv()
    BSTACK_USERNAME = os.getenv('BSTACK_USERNAME')
    BSTACK_ACCESSKEY = os.getenv('BSTACK_ACCESSKEY')
    APP_KEY = os.getenv('APP_KEY')

    if config.is_bstack:
        with allure.step('init app session'):
            options = UiAutomator2Options().load_capabilities({
                "platformName": "android",
                "platformVersion": "9.0",
                "deviceName": "Motorola Moto G7 Play",
                "app": APP_KEY,
                "appWaitActivity": "org.wikipedia.*",
                "appActivity": "org.wikipedia.main.MainActivity",
                "appPackage": "org.wikipedia.alpha",
                'bstack:options': {
                    "projectName": "Python_project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack_test",
                    'userName': BSTACK_USERNAME,
                    'accessKey': BSTACK_ACCESSKEY
                }})
            browser.config.driver = webdriver.Remote(
                config.remote_url,
                options=options)
            browser.config.timeout = float(os.getenv('timeout', '10.0'))

    else:
        options = UiAutomator2Options()
        if config.deviceName:
            options.set_capability('deviceName', config.deviceName)
        if config.appWaitActivity:
            options.set_capability('appWaitActivity', config.appWaitActivity)
        options.set_capability('app', utils.file_location.path_to_file(config.app))

        with allure.step('init app session'):
            browser.config.driver = webdriver.Remote(
                config.remote_url,
                options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    yield
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    with allure.step('tear down app session'):
        browser.quit()
    # if config.is_bstack:
    #     session_id = browser.driver.session_id
    #     utils.allure_video.attach_bstack_video(session_id)
