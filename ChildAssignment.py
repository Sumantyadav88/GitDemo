from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Sumant\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
para = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
mail = para.split("at")[1].strip().split(" ")[0]
driver.switch_to.window(WindowsOpened[0])
driver.find_element(By.NAME, "username").send_keys(mail)
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//div/select[@data-style='btn-info']").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert.alert-danger.col-md-12")))
print(driver.find_element(By.CSS_SELECTOR,".alert.alert-danger.col-md-12").text)


