from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Sumant\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#collect all vegie names => BrowserSortedveggieList (A, B, C)
browsersortedveggie=[]
list1 = driver.find_elements(By.XPATH, "//td[1]")
for veggie in list1:
    browsersortedveggie.append(veggie.text)
original_browsersortedlist = browsersortedveggie.copy() #.copy or .slice is used to make a copy of the list

#sort BrowserSortedveggieList (A, B, C) => newsorted List ->
browsersortedveggie.sort()

#check browser sorted list = new sorted list
assert original_browsersortedlist == browsersortedveggie
