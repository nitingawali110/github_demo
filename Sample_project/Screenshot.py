import time

from selenium import  webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.maximize_window()
time.sleep(5)
cont=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
cont.screenshot(".\\test.png")
cont.click()
time.sleep(5)
driver.get_screenshot_as_file("E:\\NitinPythonProject\\Sample_project\\error.png")
driver.save_screenshot(".\\test1.png")

