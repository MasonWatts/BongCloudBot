import os, requests, csv, xlsxwriter, time, shutil
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
from pathlib import Path

driver = 0

def initBrowser():
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
    return driver

def challengeBot(botName):
    driver.get("https://www.chess.com/play/computer")
    time.sleep(1)
    bots = driver.find_elements_by_class_name("bot-component")
    botFound = False
    for x in range(len(bots)):
        foundName = bots[x].get_attribute("data-bot-name")
        if foundName == botName:
            bots[x].click()
            botFound = True
            break
    if botFound:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/button").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div/div[1]/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div/div[2]/div[1]/div").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/button").click()
        time.sleep(1)
    return botFound
    

#Main--------------------

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)  

driver = initBrowser()

botFound = challengeBot("Martin-Bot")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Finish Time =", current_time)    
print("Done")