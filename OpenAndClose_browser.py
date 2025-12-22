from playwright.sync_api import sync_playwright
def open_web():
    page.goto('https://automationexercise.com/')
    page.wait_for_timeout(2000)

def close_chrome():
    chrome.close()

def close_firefox():
    firefox.close()

if __name__=='__main__':
    with sync_playwright() as sync:
        # open and close web on chrome
        chrome = sync.chromium.launch(headless=False)
        page = chrome.new_page()
        open_web()
        close_chrome()

        # open and close web on firefox
    #     firefox=sync.firefox.launch(headless=False)
    #     page=firefox.new_page()
    #     open_web()
    #     close_firefox()







