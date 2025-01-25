import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoFindElementByCSS():
    def locate_by_CSS(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys("test@yopmail.com")
        time.sleep(2)
        driver.quit()
        print("locate_by_CSS")


findbyCSS = DemoFindElementByCSS()
findbyCSS.locate_by_CSS()


class DemoFindElementLinkText():
    def locate_by_Link_Text(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Yatra for Business").send_keys("test@yopmail.com")
        time.sleep(2)
        driver.quit()
        print("locate_by_linktext")


findbyLinktext = DemoFindElementLinkText()
findbyLinktext.locate_by_Link_Text()
