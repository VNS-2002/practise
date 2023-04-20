from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/workshop/signup.php") //here//
time.sleep(10)
driver.find_element("name", "username").send_keys("vinayak")
time.sleep(10)
driver.find_element("name", "phone").send_keys("9076260354")
time.sleep(10)
driver.find_element("name", "email").send_keys("vinayak12528@gmail.com")
time.sleep(10)
driver.find_element("name", "password").send_keys("abcd1234")
time.sleep(4)

driver.find_element("name", "submit").send_keys(Keys.ENTER)
time.sleep(4)

driver.close()
print("sample test case successfully completed")
