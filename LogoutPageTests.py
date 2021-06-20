from selenium import webdriver
import MockedData
import time
import Constants
import Locators

def LogoutPageTest(username, password):
    driver = webdriver.Chrome()
    driver.get(f'{Constants.BASE_URL}{Constants.LOGIN_PAGE}')
    driver.maximize_window()

    UsernameField = driver.find_element_by_css_selector(Locators.login_page_username_css_selector)
    PasswordField = driver.find_element_by_css_selector(Locators.login_page_password_css_selector)
    LoginButton = driver.find_element_by_css_selector(Locators.login_page_login_button_css_selector)

    UsernameField.send_keys(username)
    PasswordField.send_keys(password)

    LoginButton.click()

    if driver.current_url != f'{Constants.BASE_URL}{Constants.SECURE_PAGE}': 
        print ('Unsuccessful Login')
        return

    time.sleep(4)

    logoutButton = driver.find_element_by_css_selector(Locators.logout_page_logout_button_css_selector)
    logoutButton.click()
    time.sleep(1)

    if(driver.current_url==f"{Constants.BASE_URL}{Constants.LOGIN_PAGE}"):
        print('Logout successfull')
    else:
        print('Logout failed')
    time.sleep(3)

TEST_DATA = MockedData.getTestData('MOCK_DATA.json')

for Data in TEST_DATA:

    TestLogin(Data['username'], Data['password'])
