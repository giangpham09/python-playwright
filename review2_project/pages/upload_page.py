from playwright.sync_api import Page

class UploadPage:
    # ELEMENTS
    PAGE_URL = "https://the-internet.herokuapp.com/upload"
    SELECT_BTN = "//input[@id='file-upload']"
    UPLOAD_BTN = "//input[@id='file-submit']"
    UPLOADED_FILE="//div[@class='panel text-center']"

    def __init__(self, page: Page):
        self.page = page

    def access_page(self):
        self.page.goto(self.PAGE_URL)

    def select_file(self):
        sel_file=self.page.locator(self.SELECT_BTN)
        sel_file.click()
        return sel_file

    def submit_file(self):
        self.page.locator(self.UPLOAD_BTN).click()

    def verify_uploaded_file(self):
        uploaded_file_name=self.page.locator(self.UPLOADED_FILE).inner_text()
        return uploaded_file_name