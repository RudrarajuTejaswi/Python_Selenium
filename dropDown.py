import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element(By.NAME,"name").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")
driver.find_element(By.NAME,"email").send_keys("Shetty")

driver.find_element(By.ID,"exampleCheck1").click()

#select class provide the methods to handle the options in statc dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#clicking on submit button
driver.find_element(By.XPATH,"//input[@type='submit']").click()
#retrieving the message after form submission
message = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "success" in message


#for dynamic drop downs:
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
#here find_elements is used to catch multiple items
countries=driver.find_elements(By.CSS_SELECTOR,"li[class=ui-menu-item] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
#for dynamically selected value, '.text' will not work so we use '.get_attribute("value")'{this is from DOM}
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"

