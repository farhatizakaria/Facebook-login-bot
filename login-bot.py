from selenium import webdriver
from time import sleep
from random import random as rnd
import data




class Bot:

    # Global variables
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/")
    
    
    def __init__(self,email,password):
        
        self.email = email
        self.password = password
        #self.driver = webdriver.Firefox()
        #self.driver.get("https://www.facebook.com/")
        sleep(rnd())
        
        self.driver.find_element_by_xpath('//*[@id="email"]').click()
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.email)
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="pass"]').click()
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(self.password)
        sleep(rnd())
        self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

    def logOut(self):
        """ Log out method """
        self.driver.find_element_by_xpath('//*[@id="userNavigationLabel"]').click()
        #self.driver.find_element_by_xpath('') I STOPPED HERE §§§

        # I am looking to make a method for log out




def run():
    
    emailUser = data.email
    passwordUser = data.passowrd
    Bot(emailUser,passwordUser)
    

if __name__ == '__main__':
    run()
