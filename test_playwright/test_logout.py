import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def authen_state():
    with sync_playwright() as sync:
        browser=sync.chromium.launch(headless=False)
        # create a new context with the saved storage state
        context=browser.new_context(storage_state='state.py')
        page=context.new_page()
        page.goto('https://practice.expandtesting.com/secure')
        yield page
        browser.close()

def test_logout(authen_state):
    # interact with logged-in page
    lOGOUT_BTN="//a[@href='/logout']"
    assert authen_state.locator(lOGOUT_BTN).is_visible() is True, 'Authentication State: fail!'

def test_verify_state(authen_state):
    authen_state.goto('https://practice.expandtesting.com/login')
    expect_url='https://practice.expandtesting.com/secure'
    assert authen_state.url==expect_url , 'Verify fail!'


