from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/questions/33849885/selenium-python-getting-the-current-url-of-web-browser")

url = driver.current_url
print(url)
print('123455')

driver.quit()