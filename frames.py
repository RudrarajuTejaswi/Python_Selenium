from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") #arg shud be id or name of the frame
driver.find_element(By.ID,"tinymce").text
driver.find_element(By.ID,"tinymce").clear() #clearing the content
driver.find_element(By.ID,"tinymce").send_keys("success... automated frames")
driver.switch_to.default_content() #moves back to the parent page i.e., page onload
print(driver.find_element(By.TAG_NAME,"h3").text)
#assert "WYSIWYG" in driver.find_element(By.TAG_NAME,"h3").text
driver.quit() #closes the window

