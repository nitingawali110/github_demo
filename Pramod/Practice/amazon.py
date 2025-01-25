import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Correct capitalization
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep((5))
driver.find_element(By.XPATH, "//img[@alt='Budget | Under ₹10,000']").click()
time.sleep((5))
driver.find_element(By.XPATH, "//button[@id='a-autoid-1-announce']").click()
time.sleep((5))
driver.find_element(By.XPATH, "//a[normalize-space()='Go to Cart']").click()
time.sleep((5))
driver.find_element(By.XPATH, "//input[@name='submit.delete.598c8e37-4be4-4bac-8e75-bb1c84f92f29']").click()
time.sleep((5))
# driver.minimize_window()
# driver.quit()


# driver.find_element(By.ID,"ta1").send_keys("Nitin Test Automation")
# driver.find_element(By.NAME, "q").send_keys("Nitin")
# time.sleep((10))
# driver.find_element(By.CLASS_NAME,"dropbtn").click()
# time.sleep((10))
# driver.find_element(By.LINK_TEXT,"compendiumdev").click()
# time.sleep((10))
# driver.minimize_window()
# driver.quit()

