from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

name = "Yogendra Singh"

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text
assert name in alertText
alert.accept()
#alert.dismiss()

