import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
#implicit wait is like global .. wait will be applied to all steps
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#typing ber in the search bar
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2) #to wait for page to be loaded based on search (ber)

#3.checking same list is derived
vegList_testData = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
#vegNames = driver.find_elements(By.XPATH,"//div[@class='product']/h4")
vegList_htmlData = [] # we can get this in the below for loop also
# for vegName in vegNames:
#     vegList_htmlData.append(vegName.text)
# print(vegList_htmlData)
#assert vegList_testData == vegList_htmlData

products_list = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(products_list))
for product in products_list:
    #3 testing the list of vegetables displayed
    vegList_htmlData.append(product.find_element(By.XPATH,"h4").text)
    #instead of accessing on driver we used the element, this is called chaining
    product.find_element(By.XPATH,"div/button").click()
assert vegList_testData == vegList_htmlData
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()

#1. testing total
td_total = driver.find_elements(By.XPATH, "//tr/td[4]/p")
total =0
for item_total in td_total:
    total += int(item_total.text)
total_amt = driver.find_element(By.XPATH, "//span[@class='totAmt']").text
assert total == int(total_amt)

#2.assert discount applied

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
#explicit wait is for any particular step, that takes more time
explicit_wait = WebDriverWait(driver,10) #import webDriverwait
#import expected_conditions, it has many options to select based on our requirement
explicit_wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
assert "applied" in driver.find_element(By.CLASS_NAME,"promoInfo").text

discount_amt = driver.find_element(By.XPATH, "//span[@class='discountAmt']").text
assert float(discount_amt) < float(total_amt)










