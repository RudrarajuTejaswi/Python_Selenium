import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#to open desired url in chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
#implicit wait is like global .. wait will be applied to all steps
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#typing ber in the search bar
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2) #to wait for page to be loaded based on search (ber)
products_list = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(products_list))
for product in products_list:
    #instead of accessing on driver we used the element, this is called chaining
    product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
#explicit wait is for any particular step, that takes more time
#time.sleep(10)
explicit_wait = WebDriverWait(driver,10) #import webDriverwait
#import expected_conditions, it has many options to select based on our requirement
explicit_wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
assert "applied" in driver.find_element(By.CLASS_NAME,"promoInfo").text

#explicit waits will overwrite implicit waits

