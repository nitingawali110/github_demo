import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=70130000000Enyk")

driver.maximize_window()
time.sleep(3)

dropdown=driver.find_element(By.NAME,"UserTitle")
dd=Select(dropdown)
dd.select_by_index(1)
time.sleep(3)
dd.select_by_visible_text("Marketing / PR Manager")
time.sleep(3)
dd.select_by_value("CxO_General_Manager_ANZ")
time.sleep(3)

# Get all options in the dropdown
options = dd.options

# Print each option's text
for option in options:
    print(option.text)

time.sleep(3)

driver.close()


