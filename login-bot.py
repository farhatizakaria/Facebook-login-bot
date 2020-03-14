from selenium import webdriver
from time import sleep
from random import random as rnd

emailTest = None # Write here your email
pw = 0000 # Also your password

class Bot:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com/")
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="email"]').click()
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(emailTest)
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="pass"]').click()
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(pw)
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

Bot(emailTest,pw)