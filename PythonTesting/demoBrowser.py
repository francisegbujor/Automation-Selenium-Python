from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://Google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://Espn.com")
driver.minimize_window()
driver.close()
