from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import csv
import time

browser = webdriver.Chrome()

# WE NEED TO LOG IN
login_url = 'https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin'
browser.get(login_url)

username = browser.find_element_by_id('username')
username.clear()
username.send_keys('intern.testing.email@gmail.com')
password = browser.find_element_by_id('password')
password.clear()
password.send_keys('1234ABCD')
log_in_button = browser.find_element_by_xpath('//*[@type="submit"]')
log_in_button.click()

url = 'https://www.linkedin.com/company/nike/ads/'
browser.get(url)

time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 10

while no_of_pagedowns:
    elem.send_keys(Keys.END)
    time.sleep(0.5)
    no_of_pagedowns-=1


# text_elems = browser.find_elements_by_class_name('feed-shared-update-v2__description-wrapper')

post_elems = browser.find_element_by_id("organization-ads-feed")
children = post_elems.find_elements_by_xpath("//div[@class='feed-shared-update-v2 relative full-height feed-shared-update-v2--e2e feed-shared-update--chat-ui feed-shared-update-v2--minimal-padding Elevation-2dp ember-view']")

for post in children:
    print(post.text)

