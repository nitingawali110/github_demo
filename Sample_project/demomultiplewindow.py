import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)
parent_handle = driver.current_window_handle

print(parent_handle)
driver.find_element(By.XPATH, "//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
all_window = driver.window_handles
print(all_window)

for handle in all_window:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        time.sleep(5)
        break

time.sleep(5)
driver.find_element(By.XPATH, "//button[@id='login-continue-btn']").click()
print(driver.title)

time.sleep(5)
