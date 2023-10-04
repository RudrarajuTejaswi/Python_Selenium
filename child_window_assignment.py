from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME,"blinkingText").click()
windows_list=driver.window_handles
driver.switch_to.window(windows_list[1])
mail_id = driver.find_element(By.CSS_SELECTOR,".red").text
#extracting required text
mail_id = mail_id.split(" ")
driver.switch_to.window(windows_list[0])
driver.find_element(By.ID,"username").send_keys(mail_id[4])
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
explicit_wait = WebDriverWait(driver,10)
explicit_wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"alert-danger")))
print(driver.find_element(By.CLASS_NAME,"alert-danger").text)