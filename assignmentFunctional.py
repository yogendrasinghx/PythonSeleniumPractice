import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


my_products = ['Cucumber - 1 Kg',
               'Raspberry - 1/4 Kg',
               'Strawberry - 1/4 Kg']


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)

products_infobox = driver.find_elements(By.XPATH, "//div[@class='product']")
products_name = []
for product_infobox in products_infobox:
    products_name.append(product_infobox.find_element(By.TAG_NAME, "h4").text)

assert products_name == my_products

products_cart_buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
assert len(products_cart_buttons) > 0
for add_to_cart in products_cart_buttons:
    add_to_cart.click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//div[@class='action-block']/button").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").text == "Code applied ..!"

products_amount = driver.find_elements(By.XPATH, "//tr/td[5]/p[@class='amount']")

total_products_amount = 0
for amount in products_amount:
    total_products_amount = total_products_amount + float(amount.text)


total_amount = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert total_products_amount == total_amount

discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert discounted_amount < total_amount
