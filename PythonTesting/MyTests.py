import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name = "demo"

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


driver.find_element(By.CSS_SELECTOR, "input[value='radio2']").click()
driver.find_element(By.ID, "autocomplete").send_keys("uni")
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
print("length of coutries: ", len(countries))

for country in countries:
    if country.text == "United States (USA)":
        country.click()
        break
print(driver.find_element(By.ID, "autocomplete").get_attribute("value"))
assert driver.find_element(By.ID, "autocomplete").get_attribute("value") == "United States (USA)"

driver.find_element(By.NAME, "dropdown-class-example").click()
driver.find_element(By.CSS_SELECTOR, "option[value='option3']").click()

# Handling checkboxes dynamically
checkBoxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print("length of checkboxes: ", len(checkBoxes))
for checkbox in checkBoxes:
    if checkbox.get_attribute("value") == 'option1':
        checkbox.click()
        break


# Child window
driver.find_element(By.ID, "openwindow").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "active").click()
driver.close()
driver.switch_to.window(windowsOpened[0])

# Child Tab
driver.find_element(By.ID, "opentab").click()
tabsOpened = driver.window_handles
driver.switch_to.window(tabsOpened[1])
driver.find_element(By.CLASS_NAME, "active").click()
driver.close()
driver.switch_to.window(tabsOpened[0])

# Alert button
driver.find_element(By.NAME, "enter-name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert.accept()

# Confirm button
driver.find_element(By.NAME, "enter-name").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()
confirm = driver.switch_to.alert
confirmText = confirm.text
print(confirmText)
assert name in confirmText
confirm.dismiss()

driver.find_element(By.ID, "displayed-text").send_keys("Show ME")
driver.find_element(By.ID, "hide-textbox").click()
driver.find_element(By.ID, "show-textbox").click()


courses = driver.find_elements(By.XPATH, "//table[@border='1']/tbody/tr/td[2]")
print("Length of courses: ", len(courses))
for course in courses:
    courseList = course.text
    print(courseList)

table = driver.find_elements(By.XPATH, "//div[@class='tableFixHead']//table[@id='product']")
print(len(table))
for t in table:
    print(t.text)

amountSum = 0
amount = driver.find_elements(By.XPATH, "//div[@class='tableFixHead']//table[@id='product']//tr/td[4]")
for amt in amount:
    amtText = amt.text
    amountSum = amountSum + int(amtText)
    print(amtText)
print("Sum amount: ", amountSum)

totalAmount = driver.find_element(By.CLASS_NAME, "totalAmount").text
print(totalAmount)
amountSumStr = str(amountSum)
assert amountSumStr in totalAmount


action = ActionChains(driver)
driver.execute_script("window.scrollBy(0, 1000);")
action.move_to_element(driver.find_element(By.CLASS_NAME, "mouse-hover")).perform()
action.click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 1000);")
action.move_to_element(driver.find_element(By.CLASS_NAME, "mouse-hover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
driver.execute_script("window.scrollBy(0, 1500);")

driver.switch_to.frame("courses-iframe")
action.move_to_element(driver.find_element(By.CLASS_NAME, "dropdown-toggle")).perform()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located(
    (By.XPATH, "(//a[@href='about-my-mission'][normalize-space()='About us'])[1]")))
action.move_to_element(element).click().perform()
driver.switch_to.default_content()
driver.execute_script("window.scrollTo(0, 0);")
driver.close()



while True:
    pass