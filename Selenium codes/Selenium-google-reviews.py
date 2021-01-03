# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:39:45 2020

@author: Karthik
"""
import subprocess
import csv
import time
from itertools import zip_longest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#Global initializations
url_list = [r'https://www.google.com/travel/hotels/Cardiff/entity/CgsI-tepmbaAhO7xARAB/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4452575%2C4456077%2C4458304%2C4462808%2C4463263%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517%2C4455784&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQu6e9-tyckslJEI3ozZ_ircKJiAE4AUABSAOiAQdDYXJkaWZmwAEDyAEA2gEVZW46dHJhdmVsb2RnZSBjYXJkaWZm&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBcSBwjkDxAMGBgYASgAWAGqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwiwt8vVkJvtAhUAAAAAHQAAAAAQDg',
            r'https://www.google.com/travel/hotels/Cardiff/entity/CgoIu6e9-tyckslJEAE/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4452575%2C4456077%2C4458304%2C4462808%2C4463263%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517%2C4455784&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQu6e9-tyckslJEI3ozZ_ircKJiAE4AUABSAOiAQdDYXJkaWZmwAEDyAEA2gEVZW46dHJhdmVsb2RnZSBjYXJkaWZm&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBcSBwjkDxAMGBgYASgAWAGqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwj44-G8mJvtAhUAAAAAHQAAAAAQDg',
            r'https://www.google.com/travel/hotels/Cardiff/entity/CgsIjejNn-KtwomIARAB/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4452575%2C4456077%2C4458304%2C4462808%2C4463263%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517%2C4455784&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQu6e9-tyckslJEI3ozZ_ircKJiAE4AUABSAOiAQdDYXJkaWZmwAEDyAEA2gEVZW46dHJhdmVsb2RnZSBjYXJkaWZm&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBcSBwjkDxAMGBgYASgAWAGqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwiQr67qkJvtAhUAAAAAHQAAAAAQDg',
            r'https://www.google.com/travel/hotels/Cardiff/entity/ChgIy6Th07iV-pTCARoLL2cvMXR5eXdqeGIQAQ/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4452575%2C4456077%2C4458304%2C4462808%2C4463263%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517%2C4455784&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQu6e9-tyckslJEI3ozZ_ircKJiAE4AUABSAOiAQdDYXJkaWZm2gEVZW46dHJhdmVsb2RnZSBjYXJkaWZm&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBcSBwjkDxAMGBgYASgAsAEAWAFoAZoBCRIHQ2FyZGlmZqIBEwoIL20vMDFzM3YSB0NhcmRpZmaqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwjopcb3kJvtAhUAAAAAHQAAAAAQDQ',
            r'https://www.google.com/travel/hotels/Cardiff/entity/ChgIkKXu6ejorub0ARoLL2cvMXRmMHEwem0QAQ/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4452575%2C4456077%2C4458304%2C4462808%2C4463263%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517%2C4455784&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQu6e9-tyckslJEI3ozZ_ircKJiAE4AUABSAOiAQdDYXJkaWZm2gEVZW46dHJhdmVsb2RnZSBjYXJkaWZm&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBcSBwjkDxAMGBgYASgAsAEAWAFoAZoBCRIHQ2FyZGlmZqIBEwoIL20vMDFzM3YSB0NhcmRpZmaqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwjorJf4kJvtAhUAAAAAHQAAAAAQDQ',
            r'https://www.google.com/travel/hotels/Cardiff/entity/ChgI9NLBy6Tn1-_hARoLL2cvMXRkOV8zN2YQAQ/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4452575%2C4456077%2C4458304%2C4462808%2C4463263%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517%2C4455784&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQu6e9-tyckslJEI3ozZ_ircKJiAE4AUABSAOiAQdDYXJkaWZm2gEVZW46dHJhdmVsb2RnZSBjYXJkaWZm&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBcSBwjkDxAMGBgYASgAsAEAWAFoAZoBCRIHQ2FyZGlmZqIBEwoIL20vMDFzM3YSB0NhcmRpZmaqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwjouJD5kJvtAhUAAAAAHQAAAAAQDQ'
            ]

hotel_name = ""

for url in url_list:

    #Step-1: Open chrome in debug mode on port 9222; We use subprocess module in python for this
    cmd_command = r'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Karthik\Desktop\SMA Assignment\Selenium\AutomationProfile2"'
    open_browser = subprocess.Popen(f'{cmd_command}')
    time.sleep(2)
    
    #Step-2: Initialize selenium driver to connect to the chrome window opened in step 1
        #We need to do this to tackle indefinite scrolling in the page
        #This also serves as a workaround so that chrome cannot figure out automation is opening the browser; If it does, it disables scrolling
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    options.add_argument('disable_infobars')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.get(url)
    
    #Interim-Step: This is not required. This is placed for debugging purpose if something goes wrong
    # print(browser.title)
    # session_id = browser.session_id  
    # print(session_id)
    # browser.get("https://www.google.com/travel/hotels/Cardiff/entity/CgsI-tepmbaAhO7xARAB/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4456077%2C4459385%2C4463112%2C4463263%2C4464070%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQjejNn-KtwomIARC7p7363JySyUk4AUABSAOiAQdDYXJkaWZmwAEDyAEA&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBQSBwjkDxAMGBUYASgAWAGqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwiIy-akvo_tAhUAAAAAHQAAAAAQDw")
    
    #Step-3: Scroll down 300 times on the page so that we will reach the end
        #we need to do this so that we can collect all reviews in one go
        #a wait time of 1 sec is implemented for fair-usage - this will mimic a manual user and will not put load on the website
        #we find the id of the <body> tag and send PAGE DOWN key requests to scroll
    
    no_of_pagedowns = 300
    body_tag_id = "yDmH0d"
    elem = browser.find_element_by_id(body_tag_id)  
    
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        no_of_pagedowns-=1
    
    
    #Step-4: Get required details from the page
    
    #The hotel name(branch) can be got from the browser's title
    hotel_name = browser.title

    review_block_elements = browser.find_elements_by_xpath("//div[@class='Svr5cf bKhjM']")
    
    customer=[]
    rating = []
    date =[]
    review = []
    
    customer_text = []
    review_text = []
    rating_text = []
    date_text = []

    total_count = len(review_block_elements)

    for block in review_block_elements:
        if len(block.find_elements_by_class_name("faBUBf"))> 0:
            total_count-=1
            continue
                
        print(len(block.find_elements_by_class_name("Jmi7d")))        
        if len(block.find_elements_by_class_name("Jmi7d"))> 0:
            read_more_button = []
            read_more_button = block.find_elements_by_class_name("Jmi7d")
            browser.execute_script("arguments[0].click();", read_more_button[0])
            # read_more_button[0].click()
            # webdriver.ActionChains(browser).move_to_element(read_more_button[0]).click().perform()
            time.sleep(2)
        
        # customer.append(block.find_element_by_xpath('.//a[@class="DHIhE"]'))
        print(block.find_element_by_css_selector('a.DHIhE').text)
        customer.append(block.find_element_by_css_selector('a.DHIhE'))
        rating.append(block.find_element_by_xpath('.//div[@class="KdvmLc"]'))
        date.append(block.find_element_by_xpath('.//span[@class="iUtr1"]'))
        
 
        if len(block.find_elements_by_xpath('./div[@class="kVathc"]')) > 0: #pay attention: find_element*s*
            review.append(block.find_element_by_xpath('./div[@class="kVathc"]'))
        else:
            time.sleep(2)
            review.append(block.find_element_by_xpath('./div[2]/div[1]/div[2]/div/div[1]/div/span'))
            
    for i in range(total_count):
         customer_text.append(customer[i].text)
         review_text.append(review[i].text.replace("\n",""))
         rating_text.append(rating[i].text)
         date_text.append(date[i].text)
        
    # #Consolidate all details in a list in row fashion using ZIP and then write it to a  csv file
    combined_list = list(zip_longest(customer_text, rating_text, date_text, review_text, fillvalue=""))

    with open(f"{hotel_name}.csv", "w", newline='', encoding="utf-8") as csvfile:
        scwriter = csv.writer(csvfile, delimiter="|", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        scwriter.writerow(('Customer', 'Rating_Star', 'Review_date', 'Review_Text'))
        scwriter.writerows(combined_list)
    
browser.quit()
