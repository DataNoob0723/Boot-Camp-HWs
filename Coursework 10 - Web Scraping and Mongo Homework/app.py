#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:37:59 2019

@author: zeyuyan
"""

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)
    

@app.route("/scrape")
def scraper():
    mars_info = mongo.db.mars_info
    mars_info_scraped = scrape_mars.scrape_info()
    mars_info.update({}, mars_info_scraped, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
