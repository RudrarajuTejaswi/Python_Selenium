'''here driver element scope will be only to the url given and the driver will have no knowledge
on any child tab/window opened by performing any action(say click) in the current window.
So scope of parent and child window should be explicitly mentioned'''

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()
# list wil have all windows opened in the opened order, 0-parent,2-child
windowsOpenedList = driver.window_handles
driver.switch_to.window(windowsOpenedList[1]) #switching to child window
assert driver.find_element(By.TAG_NAME,"h3").text == "New Window"
#driver.close() #---closes the opened child window
driver.switch_to.window(windowsOpenedList[0]) #going back to paret window
assert driver.find_element(By.TAG_NAME,"h3").text == "Opening a new window"
