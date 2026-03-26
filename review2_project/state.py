from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

load_dotenv()

with sync_playwright() as playwright:
    # ELEMENTS AND VALUES
    LOGIN_URL = "https://the-internet.herokuapp.com/login"
    USERNAME = "//input[@id='username']"
    PASSWORD = "//input[@id='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    username_value = os.getenv("USER_NAME")
    password_value = os.getenv("PASSWORD")
    # INTERACT WITH LOGIN PAGE
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto(LOGIN_URL)
    page.locator(USERNAME).fill(username_value)
    page.locator(PASSWORD).fill(password_value)
    page.locator(LOGIN_BUTTON).click()

    storage = context.storage_state(path="state.json")
