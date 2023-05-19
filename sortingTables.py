from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//th[@role='columnheader']").click()
names = driver.find_elements(By.XPATH, "//td[1]")
actual_names = []
for name in names:
    actual_names.append(name.text)

assert sorted(actual_names) == actual_names
