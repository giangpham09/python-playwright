import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def authen_state():
    with sync_playwright() as sync:
        browser = sync.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://thebusinessacademy.com/download-your-free-hiring-test-forms/')
        yield page
        browser.close()


def test_download(authen_state):
    # interact with upload page
    DOWNLOAD_BTN = "//a"

    # start waiting for download
    with authen_state.expect_download() as download_info:
        authen_state.locator(DOWNLOAD_BTN).click()
    download=download_info.value

    # save the downloaded file
    download.save_as("/Users/giangpham/Downloads" + download.suggested_filename)

    authen_state.wait_for_timeout(2000)





