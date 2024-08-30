import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Set up Chrome options to allow notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 1}  # 1 to allow, 2 to block
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://www.yatra.com/")

# Maximize the browser window
driver.maximize_window()

# Wait for 3 seconds to allow the page to load
time.sleep(3)

Source=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
Source.click()
time.sleep(3)
Source.send_keys("New Delhi")
time.sleep(3)
Source.send_keys(Keys.ENTER)
time.sleep(3)

Dest=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
time.sleep(3)
Dest.send_keys("New")
time.sleep(3)
search_result=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
for results in search_result:
    if "New York (JFK)" in results.text:
        results.click()
        time.sleep(4)
        break

driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//td[@id='30/09/2024']").click()

time.sleep(10)

driver.find_element(By.XPATH,"//input[@value='Search Flights']").click()

time.sleep(30)
