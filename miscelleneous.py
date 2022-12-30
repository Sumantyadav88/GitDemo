from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

Chromeoptions = webdriver.ChromeOptions()
Chromeoptions.add_argument("headless")
Chromeoptions.add_argument("--ignore-certificate-errors")

service_obj = Service("C:\Sumant\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=Chromeoptions)
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script( "window.scrollBy(0,document.body.scrollHeight);") #To run java script execute script is used
driver.get_screenshot_as_file("screen.png")
