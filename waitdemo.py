import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Sumant\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5) #5 seconds is the max time out but didn't mean that it will take complete 5 sec and it is golbally applied for whole code
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) # we used sleep here because impicit wait don't works for list as it pulls the list as soon it finds it and don't gives time to load list
Items = driver.find_elements(By.XPATH, "//div[@class='products']/div[@class='product']/div[@class='product-action']")
for Item in Items:
    Item.click()
count = len(Items)
print(count)
assert count > 0
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#explicit Wait: It is used exclusively for any particular element which is taking longer time that can't be covered in implicit

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)




