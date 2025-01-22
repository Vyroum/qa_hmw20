import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os

import config
import utils
from utils import allure_video

from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def android_app_management():
    options = UiAutomator2Options().load_capabilities({

        'platformVersion': '9.0',
        'deviceName': 'Motorola Moto G7 Play',

        'app': 'bs://sample.app',

        'bstack:options': {
            'projectName': 'Android test project for QA.GURU',
            'buildName': 'Android test build',
            'sessionName': 'Base test',

            'userName': config.bstack_userName,
            'accessKey': config.bstack_accessKey,
        }
    })

    with allure.step('Initialize app'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options
        )

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

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()
    utils.allure_video.attach_bstack_video(session_id)
