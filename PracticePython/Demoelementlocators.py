import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver=webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.ID,"login-input").send_keys("test@yopmail.com")
        time.sleep(5)
        driver.quit()
        print("locate_by_id_demo")
findbyid=DemoFindElementByID()
findbyid.locate_by_id_demo()

class DemoFindElementByNAME():
    def locate_by_name_demo(self):
        driver=webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.NAME,"login-input").send_keys("test@yopmail.com")
        time.sleep(5)
        driver.quit()
        print("locate_by_name_demo")
findbyName=DemoFindElementByNAME()
findbyName.locate_by_name_demo()