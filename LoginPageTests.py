from Constants import BASE_URL
import MockedData
from selenium import webdriver
import Constants
import Locators
import time

def TestLogin(username,password):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    LoginButton = driver.find_element_by_css_selector(Locators.home_page_login_button_css_selector)
    LoginButton.click()

    time.sleep(3)

    UsernameField = driver.find_element_by_css_selector(Locators.login_page_username_css_selector)
    PasswordField = driver.find_element_by_css_selector(Locators.login_page_password_css_selector)

    UsernameField.send_keys(username)
    PasswordField.send_keys(password)

    LoginPageLoginButton = driver.find_element_by_css_selector(Locators.login_page_login_button_css_selector)
    LoginPageLoginButton.click

    if driver.current_url == f'{Constants.BASE_URL}': 
        print(f'Login Successful with {username} and {password}')
    else:
        print(f'Login Unsuccessful with {username} and {password}')
    time.sleep(5)

TEST_DATA = MockedData.getTestData('MOCK_DATA.json')

for Data in TEST_DATA:

    TestLogin(Data['username'], Data['password'])




