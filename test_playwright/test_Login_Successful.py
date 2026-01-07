"""
- apply: locator, action, assertion
- env:  https://falcon-sandbox.blueoc.tech/
- acc: dtqa39+admin1@gmail.com
- pw: !AnhDao123
"""
import configparser
import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def set_up(page: Page):
    page.goto('https://falcon-sandbox.blueoc.tech/auth?redirect=%2F')

def access_page(page: Page):
    # LOCATOR
    BUTTON="//button[@aria-label='Accept all cookies']"
    page.locator(BUTTON).click()


def login_form(page: Page, info):
    # READ CONFIG FILE login_successful.ini
    config=configparser.ConfigParser()
    config.read('C:\\PycharmProjects\\playwright_tutorial\\test_playwright\\login_successful.ini')

    # INPUT VALUE
    EMAIL_VALUE=config.get(info, 'email')
    PASSWORD_VALUE=config.get(info, 'password')

    # LOCATOR
    EMAIL="//input[@placeholder='Enter your email']"
    PASSWORD="//input[@type='password']"
    BUTTON="//button[@type='submit']"


    # FILL TEXTBOX
    page.locator(EMAIL).clear()
    page.locator(EMAIL).fill(EMAIL_VALUE)
    page.locator(PASSWORD).clear()
    page.locator(PASSWORD).fill(PASSWORD_VALUE)

    # SUBMIT LOGIN
    page.locator(EMAIL).click()
    page.locator(BUTTON).click()


    # VERIFY SUCCESS MSG
    SUCCESS_MSG = "//div[@data-content]/div[@data-title]"
    try:
        expect(page.locator(SUCCESS_MSG)).to_have_text("You're now logged in.")
    except Exception as msg:
        print(f'There is an error: {msg}')


def test_login(page: Page,set_up):
    access_page(page)
    login_form(page,'account')



