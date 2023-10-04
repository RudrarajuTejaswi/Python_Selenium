#Alerts in java/javascript are not part of html i.e., cannot be inspected from browser

#actions-- write name in text box, click alert, assert name in alert box, click ok in alert box
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#enter data to input box in two ways
#driver.find_element(By.ID,"name").send_keys("Tejaswi")
name ="tejaswi"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
#clicking on alert button
driver.find_element(By.ID,"alertbtn").click()
#swtiching to alert window, use switch_to
alertwindow = driver.switch_to.alert
#to get the text in the alert window
print(alertwindow.text)
#to check if correct name is displayed in alert box
assert name in alertwindow.text
#to click ok button in the alert window
alertwindow.accept()
#in confirm box, we have both ok button and cancel button, to click on cancel
#alertwindow.dismiss()
