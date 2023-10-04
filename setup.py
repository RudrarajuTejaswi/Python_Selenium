from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#below way also used to open chrome, without dowloading chrome driver, this is bit slow as driver
# needs to used  from internet, not recommended as companies can block access
#service obj  is responsible for opening n closing of browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.udemy.com/")


#below way also used to open chrome, with dowloading chrome driver
service_obj = Service("C:\\Users\\chromedriver.exe") #service obj  is responsible for opening n closing of browser
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.udemy.com/")