import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//a[text()='Amazon miniTV']")
time.sleep(15)

