import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoFindElementByXpath():
    def locate_by_XPATH(self):
        driver=webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys("test@yopmail.com")
        time.sleep(2)
        driver.quit()
        print("locate_by_XPATH")

findbyXPATH=DemoFindElementByXpath()
findbyXPATH.locate_by_XPATH()