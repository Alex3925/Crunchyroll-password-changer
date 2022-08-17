import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import linecache
import time

fileacc = linecache.getline(r"emailsCR.txt",1) #takes the first line of the .txt file
filepass = linecache.getline(r"passCR.txt",1) #takes the first line of the .txt file

driver = webdriver.Edge()
driver.get("https://www.crunchyroll.com/login?next=%2F")
time.sleep(8) #To do the capatcha manually (Comment if there is no capatcha)
username = driver.find_element(By.ID, "login_form_name")
password = driver.find_element(By.ID, "login_form_password")
newpass = "ENTER_YOUR_PASSWORD_HERE"
username.send_keys(fileacc)
username.send_keys(Keys.RETURN)
password.send_keys(filepass)
driver.get("https://beta.crunchyroll.com/account/password")
currpass = driver.find_element(By.NAME, "current-password")
currpass.send_keys(filepass)
passnew = driver.find_element(By.NAME, "new-password")
passnew.send_keys(newpass)
passnew_2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/section/div/div[4]/label")
passnew_2.send_keys(newpass)
os.system("pause")
