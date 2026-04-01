import pytest
from pages.logout_page import LogoutPage

@pytest.fixture
def authen_state(browser):
    # context=browser.new_context(storage_state="state.json")
    context=browser.new_context(storage_state="/Users/giangpham/PycharmProjects/python-playwright/review2_project/state.json")
    page=context.new_page()
    page.goto("https://the-internet.herokuapp.com/secure")
    yield page
    page.close()
def test_logout(authen_state):
    logout_page = LogoutPage(authen_state)
    logout_page.access_logout_page()
    logout_page.click_logout()
    logout_msg=logout_page.get_success_msg()
    assert "You logged out of the secure area!" in logout_msg



