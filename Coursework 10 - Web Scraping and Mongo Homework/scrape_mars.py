#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:22:02 2019

@author: zeyuyan
"""

# Dependencies
from splinter import Browser
import pandas as pd


# Initialize the browser
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# Scrape information
def scrape_info():
    final_dict = dict()
    
    browser = init_browser()
    
    
    """
    Crawl news website
    """
    news_web_url = "https://mars.nasa.gov/news"
    
    browser.visit(news_web_url)
    
    news_title = browser.find_by_css('.content_title > a')[0].text
    news_p = browser.find_by_css('.article_teaser_body')[0].text
    
    print(news_title)
    print(news_p)
    print("=" * 20)
    
    final_dict["news_title"] = news_title
    final_dict["news_p"] = news_p
    
    
    """
    Crawl image website
    """
    images_web_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    
    browser.visit(images_web_url)
    
    # Click on the first image
    browser.find_by_css(".image_and_description_container")[0].click()
    
    featured_image_url = browser.find_by_css(".fancybox-image")[0]["src"]
    
    print(featured_image_url)
    print("=" * 20)
    
    final_dict["featured_image_url"] = featured_image_url
    
    
    """
    Crawl Mars weather
    """
    weather_web_url = "https://twitter.com/marswxreport?lang=en"
    
    browser.visit(weather_web_url)
    
    sections = browser.find_by_css("p.TweetTextSize.TweetTextSize--normal.js-tweet-text.tweet-text")
    
    for section in sections:
        if section.text.startswith("InSight"):
            text_to_use = section.text
            break
    
    # Remove \n
    text_to_use = text_to_use.replace("\n", " ")
    
    # Further clean
    text_to_use = text_to_use.replace("InSight ", "")
    text_to_use = text_to_use.replace("sol", "Sol")
    text_to_use = text_to_use.replace(")", "),")
    
    mars_weather = text_to_use
    
    print(mars_weather)
    print("=" * 20)
    
    final_dict["mars_weather"] = mars_weather
    
    
    """
    Crawl Mars facts
    """
    facts_web_url = "https://space-facts.com/mars/"
    
    tables = pd.read_html(facts_web_url)
    
    df = tables[0]
    
    df.columns = ["description", "value"]
    df = df.set_index("description")
    
    print(df)
    print("=" * 20)
    
    df.to_html('table.html')
    
    
    """
    Crawl Mars hemispheres
    """
    hemispheres_web_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    
    browser.visit(hemispheres_web_url)
    
    elements = browser.find_by_css("img.thumb")
    
    hemisphere_image_urls = []
    
    for i in range(len(elements)):
        store_dict = dict()
        browser.find_by_css("img.thumb")[i].click()
        title = browser.find_by_css("div.content h2.title").text
        title = title.replace(" Enhanced", "")
        img_url = browser.find_by_css("div.downloads li a")[0]["href"]
        store_dict["title"] = title
        store_dict["img_url"] = img_url
        hemisphere_image_urls.append(store_dict)
        browser.back()
    
    print(hemisphere_image_urls)
    print("=" * 20)
    
    final_dict["hemisphere_image_urls"] = hemisphere_image_urls
    
    # Close the browser after scraping
    browser.quit()
    
    return final_dict
    