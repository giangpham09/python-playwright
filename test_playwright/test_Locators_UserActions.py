import base64
import configparser
from playwright.sync_api import Page
import random

def goto_register_page(page: Page,info):

    page.goto('https://automationexercise.com/signup')

    page.get_by_placeholder('Name',exact=True).clear()
    page.get_by_placeholder('Name',exact=True).fill(f'test{random.randint(200,300)}')
    page.locator("//div[@class='signup-form']//input[@name='email']").clear()
    page.locator("//div[@class='signup-form']//input[@name='email']").fill(f'testttmail{random.randint(200, 300)}@mail.com')
    page.locator("//button[@data-qa='signup-button']").click()

    config = configparser.ConfigParser()
    config.read('C:\\PycharmProjects\\playwright_tutorial\\test_playwright\\config.ini')

    PW=config.get(info,'PW')
    FIRST_NAME=config.get(info,'FIRST_NAME')
    LAST_NAME=config.get(info,'LAST_NAME')
    COMPANY=config.get(info,'COMPANY')
    ADD1=config.get(info,'ADD1')
    ADD2=config.get(info,'ADD2')
    STATE=config.get(info,'STATE')
    CITY=config.get(info,'CITY')
    ZIPCODE=config.get(info,'ZIPCODE')
    MOBILE=config.get(info,'MOBILE')
    # LOCATORS
    # get header
    header1 = page.get_by_text('Enter Account Information').inner_text()
    header2 = page.get_by_text('Address Information').inner_text()
    print(f'The content of fist header is "{header1}"')
    print(f'The content of second header is "{header2}"')
    # get radio button
    page.get_by_label('Mr.').check()
    page.get_by_label('Mrs.').check()
    # input password
    page.get_by_role('textbox',name='password').clear()
    page.get_by_role('textbox',name='password').fill(PW)
    # select DOB
    page.locator("//select[@name='days']").select_option('2')
    page.locator("//select[@name='months']").select_option('February')
    page.locator("//select[@name='years']").select_option('2001')
    # select checkbox
    page.get_by_label('Sign up for our newsletter!',exact=True).check()
    page.get_by_label('Receive special offers from our partners!',exact=True).check()
    # input firstname, lastname, company, address, state, city, zipcode, phone
    page.get_by_role('textbox',name='First name').clear()
    page.get_by_role('textbox',name='First name').fill(FIRST_NAME)
    page.get_by_role('textbox', name='Last name').clear()
    page.get_by_role('textbox', name='Last name').fill(LAST_NAME)
    page.locator("//input[@name='company']").clear()
    page.locator("//input[@name='company']").fill(COMPANY)
    page.locator("//input[@name='address1']").clear()
    page.locator("//input[@name='address1']").fill(ADD1)
    page.locator("//input[@name='address2']").clear()
    page.locator("//input[@name='address2']").fill(ADD2)
    page.get_by_role('textbox', name='State').clear()
    page.get_by_role('textbox', name='State').fill(STATE)
    page.locator("//input[@name='city']").clear()
    page.locator("//input[@name='city']").fill(CITY)
    page.locator("//input[@name='zipcode']").clear()
    page.locator("//input[@name='zipcode']").fill(ZIPCODE)
    page.get_by_role('textbox', name='Mobile Number').clear()
    page.get_by_role('textbox', name='Mobile Number').fill(MOBILE)
    # select country
    page.get_by_label('Country').select_option('Canada')

    # screenshot element
    page.locator("//input[@name='zipcode']").screenshot(path=f"screenshot_element.png")

    # submit register form
    page.get_by_role('button',name='Create Account').click()

    # reload page by click to the logo image
    page.get_by_alt_text("Automation Exercise website").click()

    # screenshot full-page
    page.screenshot(path="screenshot_fullpage.png", full_page=True)

    page.wait_for_timeout(2000)


def test_register(page:Page):
    goto_register_page(page, 'info1')


