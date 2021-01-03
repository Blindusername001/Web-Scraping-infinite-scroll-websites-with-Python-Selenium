# Web-Scraping-infinite-scroll-websites-with-Python-Selenium

When scraping web data for reviews, one faces three major issues,
        1. Ethical issues (scraping data observing the policies of the host website to the strictest)
        2. Implementation issues
                2a. Infinite scrolling
                2b. Expand (or read more buttons)

### What is infinite scroll? 
Various examples exist for this - facebook is a popular one where new items in the feed are loaded as the user scrolls down.

### What is an expand button?
This is more common in almost all social websites. A large text is hidden so that only a small portion is available (say 200 words). If the user is interested in reading the entire text, she has to click on the expand/ read more button.

![screenshot](https://github.com/karthikkumar001/A-method-to-extract-actionable-insights-from-negative-reviews-using-NLP/blob/main/Images/2021-01-03%2020_16_24-Window.png)



If anybody is looking for a solution to this problem, chances are they are not in a position to pay for the website's API feature.

One option is to use Scrapy and send Scrapy form requests. Another option is to use selenium which is what we will do here.


## How it is achieved via selenium:

### Step-1: 
        Open chrome in debug mode on port 9222; We use subprocess module in python for this.
        If we open chrome via selenium, then the scroll option in certain websites will be deactivated.
        So we open chrome in debug mode and then capture the opened session with Selenium and then run our code on the opened browser
        To open in debug mode we need windows CMD command which is what subprocess module in python helps us with


![screenshot](https://github.com/karthikkumar001/Web-Scraping-infinite-scroll-websites-with-Python-Selenium/blob/main/Images/step1.png)



### Step-2: 
Initialize selenium driver to connect to the chrome window opened in step 1

![screenshot](https://github.com/karthikkumar001/Web-Scraping-infinite-scroll-websites-with-Python-Selenium/blob/main/Images/step2.png)



### Step-3: 
Scroll down 200 (or n) times on the page so that we will reach the end
    #we need to do this so that we can collect all reviews in one go
    #a wait time of 1 sec is implemented for fair-usage - this will mimic a manual user and will not put load on the website
    #we find the id of the \<body>\ tag and send PAGE DOWN key requests to scroll - right click on the expand element and choose inspect option on any browser to find this

![screenshot](https://github.com/karthikkumar001/Web-Scraping-infinite-scroll-websites-with-Python-Selenium/blob/main/Images/step3.png)




### Step-4: 
Find and click on the Read More buttons using selenium methods

![screenshot](https://github.com/karthikkumar001/Web-Scraping-infinite-scroll-websites-with-Python-Selenium/blob/main/Images/step4.png)


Once this is done, the user can then use a host of selenium methods to get the required information from the webpage.
The most useful methods for finding a webelement using selenium are,
        find_element_by_id
        find_element_by_class
        find_element_by_xpath
        find_element_by_css

For clicking on any element, depending on the webpage and trials, one of the following options can be used,
        <element>.click()
        webdriver.ActionChains(<webdriver>).move_to_element(<element>).click().perform()
        <webdriver>.execute_script("arguments[0].click();", <element>)
                

### Step-5: Output

Depending on your needs, you can save the output either as an excel file or a csv file. 
In this case, I used csvwriter module in python to save as a csv file.


        
        



