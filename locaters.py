from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Yogendra Singh")
driver.find_element(By.NAME, "email").send_keys("yogendra2@rahulshettyacademy.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("yogendra@zxZX12!@")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
driver.find_element(By.CSS_SELECTOR, ".ng-untouched.ng-pristine.ng-valid").clear()

# Select Static dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_visible_text('Female')
dropdown.select_by_value('male')
dropdown.select_by_index(0)

print(message)
assert "Success!" in message
input()