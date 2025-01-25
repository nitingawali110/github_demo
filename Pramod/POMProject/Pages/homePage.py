from selenium.webdriver.common.by import By
from POMProject.Locators.locators import Locators

class Homepage():
    def __init__(self,driver):
        self.driver=driver
        self.welcocme_link_id=Locators.welcocme_link_id
        self.logout_link_text=Locators.logout_link_text

    def click_welocme(self):
        self.driver.find_element(By.XPATH, self.welcocme_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_text).click()


