from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://qaclickacademy.github.io/protocommerce/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
cards = driver.find_elements(By.CSS_SELECTOR, ".card-title a")
i = -1
for card in cards:
    i = i + 1
    cardText = card.text
    print(cardText)
    if cardText == "Blackberry":
        driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
textMatch = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

assert("Success! Thank you!" in textMatch)
