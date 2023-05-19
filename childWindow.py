from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(GeckoDriverManager().install())

driver = webdriver.Firefox(service=service)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

openedWindows = driver.window_handles
driver.switch_to.window(openedWindows[1])

print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(openedWindows[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text