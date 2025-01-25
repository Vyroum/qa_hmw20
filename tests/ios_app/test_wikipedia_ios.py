import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

@pytest.mark.parametrize('mobile_os_settings',
                         [('13', 'ios', 'iPhone 11')],
                         ids=['ios'],
                         indirect=True)
def test_search_and_click(mobile_os_settings):

    with step('Searching page "Open Heart Protocol'):
        results = browser.all((AppiumBy.ACCESSIBILITY_ID, '	XCUIElementTypeTable'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Open Heart Protocol'))

    with step ('Open "Open Heart Protocol" page'):
        appium_page = results.first
        appium_page.click()