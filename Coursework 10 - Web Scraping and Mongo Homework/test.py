#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:51:34 2019

@author: zeyuyan
"""

import scrape_mars
import pymongo


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_app

mars_info_scraped = scrape_mars.scrape_info()

db.mars_info.insert(mars_info_scraped)

print(mars_info_scraped)