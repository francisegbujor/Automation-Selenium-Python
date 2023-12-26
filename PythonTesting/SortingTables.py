from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")


# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all vegetable names into browserSortedVeggieList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# sort the list into newSortedList
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList

while True:
    pass