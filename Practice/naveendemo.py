import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("Naveen Automation Lab")
time.sleep(5)

print(driver.title)
driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()