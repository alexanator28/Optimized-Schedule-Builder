'''
This scrapes the important info for the classes one imports


inputs, name of the class as list ['name', 'number']
outputs: 
        list of lists:
          [num (int), 
          type (str), 
          class # (int), 
          time (str), 
          location (str),
          Instructor (str),
          Date (str),
          waitlist (int),
          final exam time (str) (may be none if final exam was stated in an earlier num)]
'''

import os
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



baseurl = 'https://www.berkeleytime.com/catalog/'
def getinfo(name, number):
    #first make the url
    url = baseurl + name + '/' + number
    
    ### from cs50finalproject, Matt Kristoffersen 2018
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    ###

    driver = webdriver.Chrome(options=chrome_options, executable_path=os.path.abspath('chromedriver'))
    
    driver.get(url)
    driver.implicitly_wait(3)
    button = driver.find_elements_by_class_name('section-info-button')[0]
    button.click()
    driver.implicitly_wait(3)
    raw_info = driver.find_elements_by_tag_name('td')
    finish = [tag.text for tag in raw_info]
    driver.quit()
    return formatting(finish)


def formatting(lst):
    formatted = []
    #tries to make anything it can into an integer
    for i in range(len(lst)):
        try:
            formatted.append(int(lst[i]))
        except:
            formatted.append(lst[i])
    #   either if lst is empty or nothing in the list can be integerized, then it is an invalid input
    #   and we return an empty list.
    if formatted == lst:
        return []
    # grouping
    return [formatted[i:i+9] for i in range(0, len(formatted), 9) if formatted[i]]