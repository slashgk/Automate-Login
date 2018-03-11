from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.get("https://172.16.1.1:8090/")

username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")


username.send_keys("abc")
password.send_keys("xyz")

browser.find_element_by_name("btnSubmit").click()
browser.close()
