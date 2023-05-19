from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.TAG_NAME, "p").clear()
driver.find_element(By.TAG_NAME, "p").send_keys("I can type in frames")
driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME, "h3").text)