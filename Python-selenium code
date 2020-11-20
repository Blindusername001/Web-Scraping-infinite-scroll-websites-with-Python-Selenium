import subprocess
import csv
import time
from itertools import zip_longest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#Step-1: Open chrome in debug mode on port 9222; We use subprocess module in python for this
url = "https://www.google.com/travel/hotels/Cardiff/entity/CgsI-tepmbaAhO7xARAB/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4456077%2C4459385%2C4463112%2C4463263%2C4464070%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQjejNn-KtwomIARC7p7363JySyUk4AUABSAOiAQdDYXJkaWZmwAEDyAEA&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBQSBwjkDxAMGBUYASgAWAGqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwiIy-akvo_tAhUAAAAAHQAAAAAQDw"
cmd_command = r'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Karthik\Desktop\SMA Assignment\Selenium\AutomationProfile2"'
open_browser = subprocess.Popen(f'{cmd_command} {url}')
time.sleep(2)

#Step-2: Initialize selenium driver to connect to the chrome window opened in step 1
    #We need to do this to tackle indefinite scrolling in the page
    #This also serves as a workaround so that chrome cannot figure out automation is opening the browser; If it does, it disables scrolling
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument('disable_infobars')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#Interim-Step: This is not required. This is placed for debugging purpose if something goes wrong
# print(browser.title)
# session_id = browser.session_id  
# print(session_id)
# browser.get("https://www.google.com/travel/hotels/Cardiff/entity/CgsI-tepmbaAhO7xARAB/reviews?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4433754%2C4456077%2C4459385%2C4463112%2C4463263%2C4464070%2C4464463%2C4466981%2C4270859%2C4284970%2C4291517&hl=en-GB&gl=uk&un=1&ap=aAE&q=travelodge%20cardiff&rp=EPrXqZm2gITu8QEQjejNn-KtwomIARC7p7363JySyUk4AUABSAOiAQdDYXJkaWZmwAEDyAEA&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=CgUIlgEQACIDR0JQKhYKBwjkDxAMGBQSBwjkDxAMGBUYASgAWAGqAQgKBAg5GAEYAKoBFgoCCCESAggVEgIIDRICCFsSAggvGAGqAQoKAggcEgIINhgBqgESCgIIERICCEASAgg4EgIIVxgBqgEKCgIILhICCD0YAaoBCwoDCOECEgIIYxgBqgEGCgIIRhgAqgEPCgIIUBIDCIQBEgIITxgBwgECGDmSAQIgAQ&ved=0CAAQ5JsGahcKEwiIy-akvo_tAhUAAAAAHQAAAAAQDw")

print(browser.title)
session_id = browser.session_id  
print(session_id)

#Step-3: Scroll down 200 times on the page so that we will reach the end
    #we need to do this so that we can collect all reviews in one go
    #a wait time of 1 sec is implemented for fair-usage - this will mimic a manual user and will not put load on the website
    #we find the id of the <body> tag and send PAGE DOWN key requests to scroll

no_of_pagedowns = 10
body_tag_id = "yDmH0d"
elem = browser.find_element_by_id(body_tag_id)  

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    no_of_pagedowns-=1


#Step-4: There are some 

read_more_buttons = browser.find_elements_by_class_name("TJUuge")
read_more_button_count = len(read_more_buttons)
for k in range(read_more_button_count):
    element = read_more_buttons[k]
    webdriver.ActionChains(browser).move_to_element(element).click(element).perform()
#    read_more_buttons[k].click()
    time.sleep(2)


#customer
customer = browser.find_elements_by_class_name("DHIhE")
total_count = len(customer)
customer_text = []
for i in range(total_count):
    customer_text.append(customer[i].text)
    
print(customer_text)
