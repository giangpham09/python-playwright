from review2_project.pages.login_page import LoginPage
import configparser
import os

current_dir=os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_dir, "..","acc.ini")
config = configparser.ConfigParser()
config.read(config_file)

username1 = config["WrongAccount"]["username1"]
password1 = config["WrongAccount"]["password1"]
username2 = config["WrongAccount"]["username2"]
password2 = config["WrongAccount"]["password2"]
username3 = config["WrongAccount"]["username3"]
password3 = config["WrongAccount"]["password3"]
username4 = config["WrongAccount"]["username4"]
password4 = config["WrongAccount"]["password4"]
username5 = config["WrongAccount"]["username5"]
password5 = config["WrongAccount"]["password5"]

def test_login_with_wrong_password(page):
    login_page = LoginPage(page)
    login_page.fill_login_form(username3,password3)
    error_msg=login_page.get_error_msg()
    assert "Your password is invalid!" in error_msg

def test_login_with_wrong_username(page):
    login_page = LoginPage(page)
    login_page.fill_login_form(username1,password1)
    error_msg=login_page.get_error_msg()
    assert "Your password is invalid!" in error_msg
