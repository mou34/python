# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=os.environ["CHROME_DRIVER"])
browser.get(os.environ["DEV_AWSCONSOLE"])

IAM_USER = os.environ["IAM_USER"]
IAM_PASSWD = os.environ["IAM_PASSWD"]

id = browser.find_element_by_name('username')
passwd = browser.find_element_by_name('password')

id.send_keys(IAM_USER)
passwd.send_keys(IAM_PASSWD)

btn = browser.find_element_by_class_name('css3button')
btn.click()
