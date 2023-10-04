#used same scroll_screenshot.py to do in headless mode

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("headless") #runs the test without opening the browser(for faster execution)
chrome_options.add_argument("--ignore-certificate-errors") #handles certificate errors(clickicking advanced button, proxy)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#scrolling
driver.execute_script("window.scroll(0,document.body.scrollHeight)") #scroll to end of the page


#screenshot -below method takes screenshot and creates file and saves in it
driver.get_screenshot_as_file("sreenshot.png")

