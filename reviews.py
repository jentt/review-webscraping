import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from csv import writer

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.yelp.ca/biz/hollywood-pizza-and-donair-edmonton")

reviews = driver.find_elements_by_class_name("review__373c0__3MsBX")

name_text = []
star_text = []
date_text = []
comment_text = []

with open("reviews.csv", "w") as csv_file:
  csv_writer = writer(csv_file)
  headers = ["Name", "Rating", "Date", "Comment"]
  csv_writer.writerow(headers)

  for review in reviews:
    names = review.find_elements_by_class_name("css-166la90")
    stars = review.find_elements_by_xpath("/html/body/div[2]/div[2]/yelp-react-root/div[1]/div[4]/div/div/div[2]/div/div[1]/div[2]/section/div[2]/div/ul/li[2]/div/div[2]/div/div[1]/span/div")
    dates = review.find_elements_by_class_name("css-e81eai")
    comments = review.find_elements_by_class_name("raw__373c0__tQAx6")

    for name, star, date, comment in zip(names, stars, dates, comments):
      print(star.get_attribute("aria-label"))
      name_text.append(name.text)
      star_text.append(star.text)
      date_text.append(date.text)
      comment_text.append(comment.text)
      data = [(name_text), (star_text), (date_text), (comment_text)]
  csv_writer.writerows(data)
  
driver.quit()