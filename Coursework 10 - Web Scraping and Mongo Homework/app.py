#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:37:59 2019

@author: zeyuyan
"""

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route("/")
def index():
    
    mars_info = mongo.db.mars_info.find_one()
    
    if not mars_info:
        return redirect(url_for("scraper"))
    
    with open("table.html", "r") as in_file:
        table = in_file.read()

    return render_template(
            "index.html",
            mars_info=mars_info,
            table=table
    )
    

@app.route("/scrape")
def scraper():
    mars_info = mongo.db.mars_info
    mars_info_scraped = scrape_mars.scrape_info()
    mars_info.update({}, mars_info_scraped, upsert=True)
    return redirect(url_for("index"), code=302)


if __name__ == "__main__":
    app.run(debug=True)
