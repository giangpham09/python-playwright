'''
Exercise 1 — Launching and Closing a Browser
Exercise 4 — Multiple Pages in One Context
Exercise 5 — Isolated Contexts
'''

from playwright.sync_api import sync_playwright
def single_page():
    with sync_playwright() as sync:
        # Launches a browser in headless mcdode (no GUI).
        browser=sync.chromium.launch(headless=True)
        # Opens a new browser context.
        context=browser.new_context()
        # Opens one page.
        page=browser.new_page()
        # Opens one page.
        page.goto('https://www.google.com/')
        browser.close()

def multiple_pages():
    with sync_playwright() as s:
        # Launches a browser.
        browser=s.chromium.launch(headless=False)
        # Creates one browser context.
        context=browser.new_context()
        # Opens two pages (two tabs) in that context.
        page1=context.new_page()
        page2=context.new_page()
        # Navigates each page to a different URL.
        page1.goto('https://automationexercise.com/')
        page2.goto('https://playwright.dev/')
        page1.wait_for_timeout(2000)
        page2.wait_for_timeout(2000)
        # Prints both page titles.
        print(page1.title())
        print(page2.title())

def isolated_contexts():
    with sync_playwright() as sp:
        # Launch a single browser.
        browser=sp.chromium.launch(headless=False)
        # Create two separate contexts.
        context1=browser.new_context()
        context2=browser.new_context()
        # In each context, open a page and navigate to any website.
        page1=context1.new_page()
        page1.goto('https://automationexercise.com/')
        page2=context2.new_page()
        page2.goto('https://playwright.dev/')

if __name__=='__main__':
    single_page()
    multiple_pages()
    isolated_contexts()


cd