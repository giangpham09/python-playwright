'''
Verify the headers are displayed on the page 'https://automationexercise.com/signup'
'''

from playwright.sync_api import sync_playwright, expect

def set_up():
    page.goto('https://automationexercise.com/signup')

def tear_down():
    browser.close()

def verify_text():
    # get the header text
    header1=page.locator("//div[@class='login-form']//h2")
    header2=page.locator("//div[@class='signup-form']//h2")
    # Verify 'Login to your account' is visible
    expect(header1,'The text is not matched exactly for the header 1').to_have_text('Login to your account')
    # Verify 'New User Signup!' is visible
    expect(header2,'The text is not matched exactly for the header 2').to_have_text('New User Signup!')

if __name__=='__main__':
    with sync_playwright() as sync:
        browser=sync.chromium.launch(headless=False,args=["--start-maximized"])
        page=browser.new_page(no_viewport=True)
        set_up()
        verify_text()
        page.wait_for_timeout(2000)
        tear_down()



