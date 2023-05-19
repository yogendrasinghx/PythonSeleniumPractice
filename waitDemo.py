import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
assert len(products) > 0
for add_to_cart in products:
    add_to_cart.click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//div[@class='action-block']/button").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").text == "Code applied ..!"

total_amount = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert discounted_amount < total_amount
