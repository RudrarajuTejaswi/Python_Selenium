from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#1.clicking on shop tab
driver.find_element(By.LINK_TEXT,"Shop").click()
#driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click() #regex in xpath .. use contains and give a part of string
#driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click() #using regex in href.. use *

#2.grabing the phones list and adding iphone to cart
mobiles_list = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for mobile_data in mobiles_list:
    #print(mobile_data.find_element(By.XPATH,"div/h4/a").text)
    if mobile_data.find_element(By.XPATH,"div/h4/a").text == "iphone X":
        mobile_data.find_element(By.XPATH,"div[2]/button").click()

#3. checkout
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
#4.checkout -second page
driver.find_element(By.CLASS_NAME,"btn-success").click()
#5. select country (dynamic dropdown)
driver.find_element(By.ID,"country").send_keys("in")
explicit_wait = WebDriverWait(driver,20)
explicit_wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

#6. purchase the product and assert for success msg
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
success_msg = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in success_msg
driver.close()