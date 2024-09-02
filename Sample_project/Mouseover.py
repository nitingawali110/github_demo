import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)
morebutton=driver.find_element(By.XPATH,"//span[@class='more-arr']")
myaccout=driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
achains=ActionChains(driver)
achains.move_to_element(myaccout).perform()
time.sleep(5)
achains.move_to_element(morebutton).perform()
time.sleep(5)

driver.find_element(By.XPATH,"//span[normalize-space()='Trains']").click()
time.sleep(15)



