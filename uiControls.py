from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        break


radiobuttons = driver.find_elements(By.XPATH, "//fieldset/label/input[@type='radio']")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
assert not driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
