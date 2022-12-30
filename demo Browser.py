# _________________________FOR CHROME_________________________
from selenium import webdriver
#chrome driver here webdriver is the class
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\Sumant\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)  #Invoke the browser
driver.maximize_window()   #maximize the browser
driver.get("https://www.youtube.com/")    #opens the url in browser
print(driver.title)   #prints title of the browser
print(driver.current_url)    #prints url of the websites
#driver.close()         #Closes browser
driver.get("https://www.linkedin.com/company/o9solutions/mycompany/verification/")
driver.minimize_window()
driver.back()  #back to previous url
driver.forward()  #forward to next url
driver.refresh()  #refresh the url

'''#_________________FOR OTHER BROWSER


service_obj = Service("C:\Sumant")
driver = webdriver.edge(service=service_obj)

#rest all things are same in every driver
driver.maximize_window()   #maximize the browser
driver.get("https://www.youtube.com/")    #opens the url in browser
print(driver.title)   #prints title of the browser
print(driver.current_url)    #prints url of the websites
driver.close()         #Closes browser
driver.get("https://www.linkedin.com/company/o9solutions/mycompany/verification/")
driver.minimize_window()
driver.back()  #back to previous url
driver.forward()  #forward to next url
driver.refresh()  #refresh the url'''