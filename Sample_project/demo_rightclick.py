import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(3)
# achains=ActionChains(driver)
# elem1=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
# achains.context_click(elem1).perform()
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Copy']").click()

achains=ActionChains(driver)
elem2=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
achains.double_click(elem2).perform()
time.sleep(10)


