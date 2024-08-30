import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://dev.agent.innovativepartnerslp.com/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("N2010")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Test@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(15)
driver.find_element(By.XPATH,"//button[@type='button']").click()

original_window=driver.current_window_handle

all_window_handles=driver.window_handles

for handle in all_window_handles:
    if handle !=original_window:
        driver.switch_to.window(handle)
        break




# //input[@name='firstname']
#
# //label[contains(text(), 'Last Name')]
#
# //label[contains(text(), 'Email ID')]
# driver.get("https://www.example.com")
# driver.forward()
# driver.back()
# driver.refresh()
# driver.current_url
# driver.maximize_window()
# driver.delete_all_cookies()




# driver.navigate().to()
# navigate().to();
# -navigate().forward();
# -navigate().back();
# -navigate().refresh();
