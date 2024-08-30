import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://dev.agent.netwell.com/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']").send_keys("WellLifePlusAgent1002@yopmail.com")
driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']").send_keys("Test@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//span[@class='MuiButton-label']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//p[@class='jss10']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//text[normalize-space()='QUICK QUOTE']").click()
time.sleep(10)
driver.find_element(By.Id,)

# Get the window handles
original_window = driver.current_window_handle
all_windows = driver.window_handles

# Switch to the new tab
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break
# Wait for the new tab to load (adjust time as necessary)
time.sleep(15)  # Optional: wait for the page to load

# Perform actions on the new tab
print("New tab title:", driver.title)

driver.find_element(By.XPATH,"//input[@name='Zip code']").send_keys("64012")
print("64012")
time.sleep(5)
driver.find_element(By.XPATH,"//div[@id='mui-component-select-Birth Gender']").click()
time.sleep(5)
print("Click Birth Gender")
driver.find_element(By.XPATH,"//li[@data-value='M' and text()='MALE']").click()
time.sleep(3)
print("Select Male")
driver.find_element(By.XPATH,"//input[@name='Age']").send_keys("30")
print("Enter Age")
driver.find_element(By.XPATH,"//span[@class='MuiButton-label']").click()
time.sleep(10)
# Print the title of the webpage
print("Page Title:", driver.title)

# Close the browser
#driver.quit()
