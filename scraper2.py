# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd# specify the url

def get_link():
    urlpage = 'https://leetcode.com/problemset/database/' 
    # run firefox webdriver from executable path of your choice
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path = "/home/ubuntu/Baking-Bot/geckodriver")
    # get web page
    driver.get(urlpage)
    # execute script to scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    # sleep for 1s
    time.sleep(1)


    xpath = '/html/body/div/div/div/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div'
    results = driver.find_elements_by_xpath(xpath)
#    create empty array to store data
    data = []
    # loop over results
    for result in results:
       product_name = result.text
       link = result.find_element_by_tag_name('a')
       product_link = link.get_attribute("href")
       # append dict to array
       data.append({"product" : product_name, "link" : product_link})
    driver.quit()
    daily_challenge_link = data[0]['link']
    return daily_challenge_link
