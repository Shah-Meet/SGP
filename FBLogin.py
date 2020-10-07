from selenium import webdriver
from getpass import getpass
from time import sleep


def fbLogin():

    user = input('Enter your username: ')
    passwd = getpass('Enter your password: ')

    driver = webdriver.Chrome('E:\\chromedriver.exe')
    driver.get('https://www.facebook.com/login/')

    usernameBox = driver.find_element_by_id('email')
    usernameBox.send_keys(user)

    passwordBox = driver.find_element_by_id('pass')
    passwordBox.send_keys(passwd)

    logButton = driver.find_element_by_id('loginbutton')
    logButton.submit()

if __name__ == "__main__":
    fbLogin()