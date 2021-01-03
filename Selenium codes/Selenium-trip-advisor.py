# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:11:01 2020

@author: Karthik
"""

import subprocess
import csv
import time
from itertools import zip_longest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


customer_text = []
review_text = []
rating_text = []
date_text = []

url_list = [
            'https://www.tripadvisor.co.uk/Hotel_Review-g186460-d226404-Reviews-Travelodge_Cardiff_Central-Cardiff_South_Wales_Wales.html#REVIEWS'#,
            'https://www.tripadvisor.co.uk/Hotel_Review-g186460-d2039224-Reviews-Travelodge_Cardiff_Central_Queen_Street-Cardiff_South_Wales_Wales.html'#,
            'https://www.tripadvisor.co.uk/Hotel_Review-g186460-d1200491-Reviews-Travelodge_Cardiff_Atlantic_Wharf-Cardiff_South_Wales_Wales.html' #,
            'https://www.tripadvisor.co.uk/Hotel_Review-g186460-d210987-Reviews-Travelodge_Cardiff_Llanederyn-Cardiff_South_Wales_Wales.html',
            'https://www.tripadvisor.co.uk/Hotel_Review-g552071-d251187-Reviews-Travelodge_Cardiff_M4_Hotel-Pontyclun_Vale_of_Glamorgan_South_Wales_Wales.html',
            'https://www.tripadvisor.co.uk/Hotel_Review-g186460-d2232443-Reviews-Travelodge_Cardiff_Whitchurch-Cardiff_South_Wales_Wales.html'
            ]

    #Step-1: Open chrome in debug mode on port 9222; We use subprocess module in python for this
cmd_command = r'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Karthik\Desktop\SMA Assignment\Selenium\AutomationProfile3"'
open_browser = subprocess.Popen(f'{cmd_command}')
time.sleep(10)

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument('disable_infobars')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

for url in url_list:
    
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    
    
    hotel_name=""


    #Step-2: Initialize selenium driver to connect to the chrome window opened in step 1
        #We need to do this to tackle indefinite scrolling in the page
        #This also serves as a workaround so that chrome cannot figure out automation is opening the browser; If it does, it disables scrolling

    browser.get(url)
    time.sleep(10)
    browser.maximize_window()
    
    #Interim-Step: This is not required. This is placed for debugging purpose if something goes wrong
    # print(browser.title)
    # session_id = browser.session_id  
    # print(session_id)
    # browser.get("https://www.google.com/travel/hotels/Cardiff/entity/CgsI-tepmbaAhO7xARAB/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4456077%2C4459385%2C4463112%2C4463263%2C4464070%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQjejNn-KtwomIARC7p7363JySyUk4AUABSAOiAQdDYXJkaWZmwAEDyAEA&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBQSBwjkDxAMGBUYASgAWAGqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwiIy-akvo_tAhUAAAAAHQAAAAAQDw")
    
    hotel_name = browser.title
        
    #Step-3: #we need to do this so that we can collect all reviews in one go
        #a wait time of 1 sec is implemented for fair-usage - this will mimic a manual user and will not put load on the website
        #we find the id of the <body> tag and send PAGE DOWN key requests to scroll
    
    #privacy_ok_button = browser.find_element_by_id("_evidon-accept-button")
    #webdriver.ActionChains(browser).move_to_element(privacy_ok_button).click(privacy_ok_button).perform()
    #time.sleep(2)
    
    page_elements = browser.find_elements_by_class_name("pageNum")
    total_pages = int(page_elements[-1].text)
    print(total_pages)
    
    for page in range(2,total_pages+1): 
    
        read_more_buttons = browser.find_elements_by_class_name("_3maEfNCR")
        element = read_more_buttons[0]
        webdriver.ActionChains(browser).move_to_element(element).click(element).perform()
        time.sleep(2)
        
        #customer
        customer = browser.find_elements_by_xpath('//a[@class="ui_header_link _1r_My98y"]')
        #review
        review = browser.find_elements_by_class_name("IRsGHoPm")
        #rating        
        rating_parent_class = "nf9vGX55"
        rating =  browser.find_elements_by_xpath(f'//div[@class="{rating_parent_class}"]/span')
        #date
        date = browser.find_elements_by_xpath('//a[@class="ui_header_link _1r_My98y"]/..')
        
        
        for i in range(0,5):
             customer_text.append(customer[i].text)
             review_text.append(' '.join([line for line in review[i].text.split("\n") if line.strip() != ""]))
             rating_text.append(rating[i].get_attribute("class"))
             date_text.append(date[i].text)
        
        no_of_pagedowns = 3
        body_tag_id = "BODY_BLOCK_JQUERY_REFLOW"
        elem = browser.find_element_by_id(body_tag_id)  
        
        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            no_of_pagedowns-=1
        
        # next_page_button = browser.find_elements_by_xpath(f"//a[@class='pageNum' and text()={page}]")
        print((f"//div[@class='pageNumbers']/a[text()='{page}']"))
        
        next_page_button = browser.find_elements_by_xpath(f"//div[@class='pageNumbers']/a[text()='{page}']")
        print(next_page_button)
        next_page_button[0].click()
        time.sleep(3)
    
    
    combined_list = list(zip_longest(customer_text, rating_text, date_text, review_text, fillvalue=""))
    print(combined_list)
    
    with open(f"{hotel_name}.csv", "w", newline='', encoding="utf-8") as csvfile:
        scwriter = csv.writer(csvfile, delimiter="|", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        scwriter.writerow(('Customer', 'Rating_Star', 'Review_date', 'Review_Text'))
        scwriter.writerows(combined_list)
    
browser.close()
browser.quit()
