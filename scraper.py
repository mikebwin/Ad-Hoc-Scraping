from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time

handle_name_list = []
file = open("handles.txt", "r")
for line in file:
    handle_name_list.append(line)
file.close()

browser = webdriver.Chrome()
results_list = []

# if you want to capture more, add the keys in this list
keys = ["influencer", "posts", "followers", "following"]

count = 0
multiple = 1

for handle_name in handle_name_list:
    # okay so this was just the quickest fix i could do
    # if any time you wanna quit, everything done up to that point is saved
    try:
        url = "https://www.instagram.com/" + handle_name + "/"
        browser.get(url)
        html = browser.page_source

        soup = BeautifulSoup(html, 'html.parser')
        info_list = soup.findAll('span', {"class": "g47SY"})

        # this process is just to clean up the string, i.e. remove commas
        # and also to cast as an int
        info = dict({'influencer': handle_name.strip()})
        info['posts'] = int(info_list[0].text.replace(",", ""))
        info['followers'] = int(info_list[1].get("title").replace(",", ""))
        info['following'] = int(info_list[2].text.replace(",",""))

        results_list.append(info)
        count += 1
        if count > (multiple * 100):
            multiple += 1
            time.sleep(30)
    except:
        pass

# after either an error or finishing the run, write to this file
# 'w+' will overwrite everything in results.csv
f = open("results.csv", "w+")
dict_writer = csv.DictWriter(f, keys)
dict_writer.writeheader()
dict_writer.writerows(results_list)
f.close()

