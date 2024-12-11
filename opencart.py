import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://demo.opencart.com/en-gb?route=account/register")
driver.maximize_window()
time.sleep(10)
driver.close()