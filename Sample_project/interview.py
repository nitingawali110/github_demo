import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class google():

    def sample_test(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH,"//textarea[@name='q']").send_keys("Seleninum")
        time.sleep(5)

obj=google()
obj.sample_test()


b=10
a=5
data=lambda b=b:b+a
print(data())


