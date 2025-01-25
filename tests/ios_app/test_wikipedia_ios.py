import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

@pytest.mark.parametrize('mobile_os_settings',
                         [('13', 'ios', 'iPhone 11')],
                         ids=['ios'],
                         indirect=True)
def test_search_and_click(mobile_os_settings):
    with step('Input text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()

        input_text = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input'))
        input_text.type('qa.guru lesson 19').press_enter()

    with step('Checking input text'):
        text_output = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output'))
        text_output.should(have.text('qa.guru lesson 19'))