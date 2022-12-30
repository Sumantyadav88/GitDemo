

ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2: #raise Exception("Products Cart count not matching")
    pass

assert(ItemsInCart == 0)  #It should always true otherwise it will break test

#try , catch

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except:
    print("SOme how i reached this block because there is failure in try block")


try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:  #It will give error which python gives
    print(e)

finally:
    print("cleaning up records")



from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service

service_obj= Service("C:\Sumant")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://www.youtube.com/")
