from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")
driver.implicitly_wait(5)
name = driver.find_element_by_id('username')
passcode = driver.find_element_by_id('password')
driver.implicitly_wait(5)
name.send_keys('####')                #enter your id here
passcode.send_keys('####')      #enter your passcode here
driver.implicitly_wait(5)
submit = driver.find_element_by_id('loginbtn')
submit.click()
driver.implicitly_wait(5)

text = driver.find_elements_by_class_name("ml-1")
for i in text:
    print(i.text)