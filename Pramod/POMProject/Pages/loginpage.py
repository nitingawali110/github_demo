from selenium.webdriver.common.by import By
from POMProject.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_textbox_id = Locators.login_button_textbox_id
        self.invalid_username_message_xpath= "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_textbox_id).click()

    def check_invalid_usename_message(self):
        msg=self.driver.find_element(By.XPATH,self.invalid_username_message_xpath).text
        return msg
