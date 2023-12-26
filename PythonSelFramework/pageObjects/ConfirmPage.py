from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchaseItems(self):
        return self.driver.find_element(*ConfirmPage.purchase)