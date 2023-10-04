from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#to open desired url in chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
#check box can be selected using ID or whatever, this case is like: what if options in the check box are not fixed and
# we want to select a particular value(say option2)
# we used find_elements to get all the check boxes
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        #is_selected method on check boxes used to confirm whether selection is done
        assert checkbox.is_selected()

radiobuttons = driver.find_elements(By.NAME,"radioButton")
#here its an example where the position of items will not change then we can directly use the index instead of running
# a for loop
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


#hide and show based on button click
assert driver.find_element(By.ID,"displayed-text").is_displayed()

driver.find_element(By.ID,"hide-textbox").click()

assert not driver.find_element(By.ID,"displayed-text").is_displayed()




