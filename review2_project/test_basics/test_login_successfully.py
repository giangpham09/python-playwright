from review2_project.pages.login_page import LoginPage
import os

def test_login_successfully(page):
    login_page=LoginPage(page)
    # GO TO LOGIN PAGE
    login_page.access_login_page()

    # SET ENVIRONMENT VARIABLES ON .env file
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    # FILL LOGIN FORM
    login_page.fill_login_form(username,password)

    # VERIFY MSG AFTER LOGIN SUCCESS
    success_msg=login_page.get_success_msg()
    assert "You logged into a secure area!" in success_msg




