from playwright.sync_api import Page

class DownloadPage:
    # ELEMENTS
    PAGE_URL="https://the-internet.herokuapp.com/download"
    JPG_FILE="//a[@href='download/sm.jpg']"
    TXT_FILE="//a[@href='download/sample_upload.txt']"
    ZIP_FILE="//a[@href='download/sample-zip-file.zip']"
    CSV_FILE="//a[@href='download/report.csv']"

    def __init__(self, page: Page):
            self.page = page

    def access_page(self):
        self.page.goto(self.PAGE_URL)

    def download_JPG(self):
        self.page.locator(self.JPG_FILE).click()

    def download_TXT(self):
        self.page.locator(self.TXT_FILE).click()

    # def get_download_path(self):