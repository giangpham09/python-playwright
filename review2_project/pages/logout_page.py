from playwright.async_api import Page

class LogoutPage:
    # ELEMENTS
    LOGOUT_URL="https://the-internet.herokuapp.com/secure"
    LOGOUT_BTN="//a[@class='button secondary radius']"
    LOGOUT_MSG="//div[@class='flash success']"

    def __init__(self,page: Page):
        self.page = page

    # ACTIONS
    def access_logout_page(self):
        self.page.goto(self.LOGOUT_URL)

    def click_logout(self):
        self.page.locator(self.LOGOUT_BTN).click()

    def get_success_msg(self):
        return self.page.locator(self.LOGOUT_MSG).text_content()

