# webpage login practice. Getting login credentials from child website
# attempt on parent site
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME, "blinkingText").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
result = driver.find_element(By.CLASS_NAME, "im-para.red").text
print(result.split())
retrievedEmail = result.split()
email = str(retrievedEmail[4])

driver.switch_to.window(windowsOpened[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("pass123")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@style='display: block;']")))
alert = driver.find_element(By.XPATH, "//div[@style='display: block;']").text
alertMessage = "Incorrect username/password."
print("Alert: ", alert)
assert alertMessage == alert


while True:
    pass
