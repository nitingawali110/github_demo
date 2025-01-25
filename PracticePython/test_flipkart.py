import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Fixture to initiate the Selenium WebDriver for browser interaction
@pytest.fixture(scope="module")
def setup_browser():
    # Replace the path to the location where your browser driver is located
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Test 1: Open Flipkart.com and assert the URL or an element
def test_flipkart_url(setup_browser):
    driver = setup_browser
    driver.get("https://www.flipkart.com/")

    # Assert that the URL contains 'flipkart'
    assert "flipkart.com" in driver.current_url, "Flipkart URL is incorrect"
    assert "Online Shopping Site" in driver.title, "Title is not correct"
    print("title",driver.title)

    cart_icon = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
    assert cart_icon.is_displayed(), "Cart icon is not displayed"

    assert "Cart" in cart_icon.text, "Cart icon text does not contain 'Cart'"

    Login_button=driver.find_element(By.XPATH, "//span[normalize-space()='Login']")
    assert Login_button.is_displayed(), "Login button is not displayed"

    #login=//span[normalize-space()='Login']
    # Optionally, assert an element on the page (e.g., search bar element)
    search_bar = driver.find_element(By.NAME, "q")
    assert search_bar.is_displayed(), "Search bar is not displayed"

    # Find the image element using XPath
    img_element = driver.find_element(By.XPATH, "//img[contains(@alt, 'Mobiles')]")

    # Assert that the image is displayed
    assert img_element.is_displayed(), "Image with alt 'Mobiles' is not displayed on the page!"
    img_element.click()

    time.sleep(10)

# Test 2: Using requests library to check status code
def test_flipkart_status_code():
    url = "https://www.google.com/"
    response = requests.get(url)
    print(response.status_code)
#
#     Assert that the status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
