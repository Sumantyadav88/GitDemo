from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("--start-maximized")
ChromeOptions.add_argument("headless")
ChromeOptions.add_argument("--ignore-certificate-errors")
service_obj = Service("C:\Sumant\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options = ChromeOptions)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)

