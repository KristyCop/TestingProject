import MockedData
from selenium import webdriver
import Constants
import Locators
import time

def TestRegistration(username,email,password):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    HomeLoginButton = driver.find_element_by_css_selector(Locators.home_page_login_button_css_selector)
    HomeLoginButton.click()

    RegisterButton = driver.find_element_by_css_selector(Locators.login_page_register_button_css_selector)
    RegisterButton.click()

    UsernameField = driver.find_element_by_css_selector(Locators.registration_page_username_css_selector)
    EmailField = driver.find_element_by_css_selector(Locators.registration_page_email_css_selector)
    PasswordField = driver.find_element_by_css_selector(Locators.registration_page_password_css_selector)
    Password2Field = driver.find_element_by_css_selector(Locators.registration_page_password2_css_selector)
    RegisterButton = driver.find_element_by_css_selector(Locators.registration_page_register_button_css_selector)
    
    UsernameField.send_keys(username)
    EmailField.send_keys(email)
    PasswordField.send_keys(password)
    Password2Field.send_keys(password)

    RegisterButton.click()
    time.sleep(3)
    
    SuccessfullRegistration = driver.find_element_by_css_selector(Locators.registration_page_successfull_registration_button_css_selector)
    time.sleep(3)

    if SuccessfullRegistration.text=='OK': 
        print(f'Registration Successful with {email}  and {username} and {password}')
    else:
        print(f'Registration Unsuccessful with {email}  and {username} and {password}')
    time.sleep(3)

TEST_DATA = MockedData.getTestData('MOCK_DATA.json')

for Data in TEST_DATA:

    TestRegistration(Data['username'], Data['email'], Data['password'])
