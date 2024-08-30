import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
driver.maximize_window()
time.sleep(2)
# Switch with ifrmae Locator
#driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
# switch with ID
driver.switch_to.frame("iframeResult")
# switch with name
#driver.switch_to.frame("iframeResult")
# switch with index
time.sleep(3)
#driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//a[@title='HTML Tutorial']").click()
time.sleep(3)


