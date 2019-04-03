#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:23:42 2019

@author: zeyuyan
"""

# Import necessary libraries
from flask import Flask, jsonify
from app_utils import data_last_year_dict, station_dict, data_tobs_dict, calc_temps_start, calc_temps_start_end

app = Flask(__name__)


@app.route("/")
def home():
    return (
            "<h1>Welcome to the Climate App API!</h1><br/>"
            "<h2>Available Routes:<h2><br/>"
            "/api/v1.0/precipitation<br/>"
            "/api/v1.0/stations<br/>"
            "/api/v1.0/tobs<br/>"
            "/api/v1.0/&ltstart&gt<br/>"
            "/api/v1.0/&ltstart&gt/&ltend&gt"
            )

@app.route("/api/v1.0/precipitation")
def prcp_jsonified():
    return jsonify(data_last_year_dict)

@app.route("/api/v1.0/stations")   
def stations_jsonified():
    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def tobs_jsonified():
    return jsonify(data_tobs_dict)

@app.route("/api/v1.0/<start>")
def temp_start(start):
    results_list = calc_temps_start(start)
    results_dict = {
            "TMIN": results_list[0][0],
            "TAVG": results_list[0][1],
            "TMAX": results_list[0][2],
            }
    return jsonify(results_dict)

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    results_list = calc_temps_start_end(start, end)
    results_dict = {
            "TMIN": results_list[0][0],
            "TAVG": results_list[0][1],
            "TMAX": results_list[0][2],
            }
    return jsonify(results_dict)
    
    


if __name__ == "__main__":
    app.run(debug=True)
