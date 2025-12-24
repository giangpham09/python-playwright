from Tools.scripts.generate_opcode_h import footer
from playwright.sync_api import sync_playwright

# HARD WAIT: open page and wait for 2s
def hard_wait():
    page.goto('https://automationexercise.com/')
    page.wait_for_timeout(2000)


# DYNAMIC WAIT:
# wait for the page is loaded all
def wait_loaded():
    page.goto('https://automationexercise.com/contact_us')
    # waiting for page load
    page.wait_for_load_state('load')
    # action after page load done
    page.locator("//input[@id='susbscribe_email']").scroll_into_view_if_needed()
    # wait to see the action
    page.wait_for_timeout(2000)

# wait for the error message is displayed
def wait_error():
    page.goto('https://automationexercise.com/login')
    page.get_by_placeholder('Password',exact=True).clear()
    page.get_by_placeholder('Password',exact=True).fill('kd343')
    page.locator("//div[@class='login-form']//input[@name='email']").clear()
    page.locator("//div[@class='login-form']//input[@name='email']").fill('test_undel@example.com')
    page.locator("//button[@data-qa='login-button']").click()
    # wait error msg displayed then get the msg
    error_msg=page.wait_for_selector("//p", state="visible").inner_text()
    print(error_msg)
    page.wait_for_timeout(2000)

if __name__=='__main__':
    with sync_playwright() as sync:
        browser = sync.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)
        hard_wait()
        wait_loaded()
        wait_error()

