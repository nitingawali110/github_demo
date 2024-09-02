import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/tyy/4io/~cs-6i0duusqlz/pr?sid=tyy%2C4io&collection-tab-name=Realme+P1+5g&param=6372&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTE0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSBQMSA1ZyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdZUTZCWFNFTlpSVjMiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax")
driver.maximize_window()
time.sleep(3)


elem1=driver.find_element(By.XPATH,"//div[@class='iToJ4v Kaqq1s']//div[@class='PYKUdo']")
elem2=driver.find_element(By.XPATH,"//div[@class='iToJ4v D0puJn']//div[@class='PYKUdo']")
achains=ActionChains(driver).drag_and_drop_by_offset(elem1,90,0).perform()
time.sleep(10)
achains=ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(50,0).release().perform()
time.sleep(10)
