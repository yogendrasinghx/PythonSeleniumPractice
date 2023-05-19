from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

product_name = "Nokia Edge"
home_country = "India"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/shop")

product_box = driver.find_elements(By.TAG_NAME, "app-card")

for product in product_box:
    if product.find_element(By.TAG_NAME, "h4").text == product_name:
        product.find_element(By.TAG_NAME,"button").click()
        break
driver.find_element(By.XPATH, "//div[@id='navbarResponsive']/ul/li/a").click()

assert product_name == driver.find_element(By.LINK_TEXT, product_name).text

driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
driver.find_element(By.ID, "country").send_keys(home_country)

wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']")))
driver.find_element(By.XPATH, "//div[@class='suggestions']/ul/li/a[text()='"+home_country+"']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "label[for='checkbox2']")))
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.XPATH, " //input[@value='Purchase']").click()

assert "Success! Thank you!" in driver.find_element(By.CSS_SELECTOR, ".alert-success").text