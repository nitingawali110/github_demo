import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Correct capitalization
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.find_element(By.ID,"ta1").send_keys("Nitin Test Automation")
time.sleep((10))
driver.find_element(By.NAME, "q").send_keys("Nitin")
time.sleep((10))
driver.find_element(By.CLASS_NAME,"dropbtn").click()
time.sleep((10))
driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep((10))












# paraent_window_id=driver.current_window_handle
#
# driver.find_element(By.XPATH,"//a[normalize-space()='Open a popup window']").click()
# windows=driver.window_handles
#
# for w in windows:
#     driver.switch_to.window(w)
#     if driver.title.__eq__("New Window"):
#         para_one_text=driver.find_element(By.XPATH,"//h3[normalize-space()='New Window']").text
#         print(para_one_text)
#         driver.close()
#         break
#
# driver.switch_to.window(paraent_window_id)

# time.sleep((10))
# driver.find_element(By.CLASS_NAME,"dropbtn").click()
# time.sleep((10))
# driver.find_element(By.LINK_TEXT,"compendiumdev").click()
time.sleep((10))
driver.minimize_window()
driver.quit()

