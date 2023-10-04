from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#scrolling
driver.execute_script("window.scroll(0,document.body.scrollHeight)") #scroll to end of the page
driver.execute_script("window.scroll(0,0)") #scroll to top again
driver.execute_script("window.scroll(0,500)") #scroll to y-axis=500

#screenshot -below method takes screenshot and creates file and saves in it
driver.get_screenshot_as_file("sreenshot.png")

