#1. import ActionChains for mouse actions and pass driver object and give perform() at end
#2. with this actionChains we can check double clicking a checkbox and many
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
#driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

mouse_handle = ActionChains(driver)
#mouse_handle.double_click() ---------for double clicking
#mouse_handle.context_click() -----for right click
#mouse_handle.drag_and_drop() -----for drag n drop functionality, source and dest shud be given
#perform() is mandatory for all mouse_handle events
mouse_handle.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#mouse_handle.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
mouse_handle.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()



