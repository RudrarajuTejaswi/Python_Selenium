from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//tr/th[1]").click()
print("************************") #keep a break point here and sort again on web page
vegNames = driver.find_elements(By.XPATH,"//tr/td[1]")
print(len(vegNames))
veg_list =[x.text for x in vegNames] #grabbing the web sorted list
sorted_veg_list = sorted(veg_list) #doing a python sort on it
assert veg_list == sorted_veg_list
