import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from POMProject.Pages.loginpage import LoginPage
from POMProject.Pages.homePage import Homepage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username("Admin")
        time.sleep(3)
        login.enter_password("admin123")
        login.click_login()
        time.sleep(5)
        homepage = Homepage(driver)
        homepage.click_welocme()
        time.sleep(5)
        homepage.click_logout()

    def test_02_login_invalid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username("Admin1")
        time.sleep(3)
        login.enter_password("admin123")
        login.click_login()
        time.sleep(3)
        message = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        self.assertEqual(message, "Invalid credentials")

        # self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-userdropdown')]").click()
        # time.sleep(3)
        # # driver.find_element(By.XPATH, "//a[text()='Logout']").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
        # time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '--main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/PythonProject/pythonProject/POMProject/Report'))
