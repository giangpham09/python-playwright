import configparser
import pytest
from playwright.sync_api import Page,expect

@pytest.fixture
def set_up(page: Page):
    page.goto('https://falcon-sandbox.blueoc.tech/auth?redirect=%2F')

def access_page(page: Page):
    # LOCATOR
    BUTTON="//button[@aria-label='Accept all cookies']"
    page.locator(BUTTON).click()

def login_form(page: Page, info):
    # READ CONFIG FILE login_unsuccessful.ini.ini
    config=configparser.ConfigParser()
    config.read('C:\\PycharmProjects\\playwright_tutorial\\test_playwright\\login_unsuccessful.ini')

    # INPUT VALUE
    EMAIL_VALUE = config.get(info, 'email')
    PASSWORD_VALUE = config.get(info, 'password')

    # LOCATOR
    EMAIL = "//input[@placeholder='Enter your email']"
    PASSWORD = "//input[@type='password']"
    BUTTON = "//button[@type='submit']"
    EMAIL_ERROR_MSG = "//p[@class='mt-2 text-sm text-[#F97066] text-left']"
    PW_ERROR_MSG = "//span[class='text-sm font-medium']"

    # FILL TEXTBOX
    page.locator(EMAIL).clear()
    page.locator(EMAIL).fill(EMAIL_VALUE)
    page.locator(PASSWORD).clear()
    page.locator(PASSWORD).fill(PASSWORD_VALUE)



    # SUBMIT LOGIN
    try:
        if page.locator(BUTTON).is_enabled():
            page.locator(BUTTON).click()
            if page.locator(EMAIL_ERROR_MSG).is_visible():
                pass
            elif page.locator(PW_ERROR_MSG).is_visible():
                pass
        elif page.locator(BUTTON).is_disabled():
            pass

    except Exception as msg:
        print(f'There is an error: {msg}')

def test_empty_textbox(page: Page,set_up):
    access_page(page)
    login_form(page,'WrongAccount1')
    login_form(page,'WrongAccount2')
    login_form(page,'WrongAccount3')
    login_form(page,'WrongAccount4')
    login_form(page,'WrongAccount5')
    login_form(page,'WrongAccount6')
    login_form(page,'WrongAccount7')



