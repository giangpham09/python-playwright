from playwright.sync_api import Page

class LoginPage:
    # ELEMENTS
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = "//input[@id='username']"
    PASSWORD = "//input[@id='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    LOGIN_MSG="//div[@class='flash success']"
    ERROR_MSG="//div[@class='flash error']"

    def __init__(self,page: Page):
        self.page = page

    # ACTIONS
    def access_login_page(self):
        self.page.goto(self.URL)

    def fill_login_form(self,username,password):
        # FILL VALUES TO THE TEXTBOXES
        self.page.locator(self.USERNAME).fill(username)
        self.page.locator(self.PASSWORD).fill(password)
        # CLICK SUBMIT BUTTON
        self.page.locator(self.LOGIN_BUTTON).click()

    def get_success_msg(self):
        return self.page.locator(self.LOGIN_MSG).text_content()

    def get_error_msg(self):
        return self.page.locator(self.ERROR_MSG).text_content()













