#!/usr/bin/env python
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://meet.google.com/xxx-xxxx-xxx'

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.microphone', 2) # disable microphone
firefox_profile.set_preference('permissions.default.camera', 2) # disable camera

options = Options()

options.headless = True # no need for ui

browser = webdriver.Firefox(firefox_profile=firefox_profile)

browser.get('https://www.google.com/accounts/Login') # login page
browser.find_element_by_id("identifierId").send_keys("email")
browser.find_element_by_id("identifierNext").click()
time.sleep(1)
browser.find_element_by_name("password").send_keys("passwd")
browser.find_element_by_id("passwordNext").click()
browser.get(url)
time.sleep(5)
browser.find_element_by_xpath("//span[contains(text(),'Join now')]").click()

print("logged")

while True:
    time.sleep(1)
