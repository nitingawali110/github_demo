import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
driver.maximize_window()
URL=driver.current_url
print(URL)
time.sleep(2)
driver.switch_to.frame("iframeResult")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
time.sleep(5)
alert = driver.switch_to.alert
print("Alert message:", alert.text)
driver.switch_to.alert.accept()

URL=driver.current_url

#driver.switch_to.alert.dismiss()

