from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("screenshot.png")