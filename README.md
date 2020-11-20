*******Needs to be updated with a proper description***********

# Web-Scraping-infinite-scroll-websites-with-Python-Selenium
Providing a completely automated web scraping solution for websites having infinite scroll (i.e.) new items appear as user scrolls down instead of page numbers

This is achieved by using Python and selenium.

How it is achieved:

Step-1: Open chrome in debug mode on port 9222; We use subprocess module in python for this

Step-2: Initialize selenium driver to connect to the chrome window opened in step 1
    #We need to do this to tackle indefinite scrolling in the page
    #This also serves as a workaround so that chrome cannot figure out automation is opening the browser; If it does, it disables scrolling

Step-3: Scroll down 200 times on the page so that we will reach the end
    #we need to do this so that we can collect all reviews in one go
    #a wait time of 1 sec is implemented for fair-usage - this will mimic a manual user and will not put load on the website
    #we find the id of the <body> tag and send PAGE DOWN key requests to scroll

  
