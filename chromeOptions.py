from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #for not closing browser once execution is done
chrome_options.add_argument("headless") #runs the test without opening the browser(for faster execution)
chrome_options.add_argument("--ignore-certificate-errors") #handles certificate errors(clickicking advanced button, proxy)
chrome_options.add_argument("--start-maximized") #to open window maximized, can use this instead of driver.maximize()
chrome_options.add_argument("--disable-gpu") #improves performance
driver= webdriver.Chrome(options=chrome_options)

#it has all info
#https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions