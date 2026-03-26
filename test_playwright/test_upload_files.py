import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def authen_state():
    with sync_playwright() as sync:
        browser=sync.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://qa-automation-practice.netlify.app/file-upload')
        yield page
        browser.close()

def test_upload(authen_state):
    # interact with upload page
    SELECT_BTN="//input[@id='file_upload']"
    SUBMIT_BTN="//button[@type='submit']"

    # select one file
    authen_state.locator(SELECT_BTN).set_input_files('Waits.py')
    authen_state.locator(SUBMIT_BTN).click()

    # select multiple files: take files to the list
    authen_state.locator(SELECT_BTN).set_input_files(['/Users/giangpham/Downloads/23dae0c6e1697bd4a2b2e45d0c1625d6.jpg'])
    authen_state.locator(SUBMIT_BTN).click()

    # remove all the selected files
    authen_state.locator(SELECT_BTN).set_input_files([])
    authen_state.locator(SUBMIT_BTN).click()

    authen_state.wait_for_timeout(2000)





