import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Correct capitalization
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
testfield=driver.find_element(By.XPATH,"//input[@id='textbox1']")
testfield.clear()
time.sleep(2)
testfield.send_keys("Nitin Gawali")
time.sleep(2)
testfield.clear()
time.sleep(2)
testfield.send_keys("Automation")
time.sleep(2)

driver.quit()
