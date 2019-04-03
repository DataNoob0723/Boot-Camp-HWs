#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:04:18 2019

@author: zeyuyan
"""

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
import datetime as dt


engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


# Find the list of stations
station_list_to_use = session.query(Station.station, Station.name).all()
station_dict = dict(station_list_to_use)

# Find the station with the most amount of data
sorted_results_list = session.query(Measurement.station, func.count(Measurement.station))\
                                .group_by(Measurement.station)\
                                .order_by(func.count(Measurement.station).desc()).all()

my_station = sorted_results_list[0][0]

end_date = session.query(Measurement.date).\
                   filter(Measurement.station == my_station).\
                   order_by(Measurement.date.desc()).first()[0]

end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')
begin_date = end_date - dt.timedelta(days=365)

data_last_year = session.query(Measurement.date, Measurement.prcp)\
                 .filter(and_(Measurement.station == my_station,
                              Measurement.date >= begin_date,
                              Measurement.date <= end_date,)).all()
                 
data_last_year_dict = dict(data_last_year)

# Find the id of the last datapoint
id_last = session.query(func.max(Measurement.id)).all()[0][0]
station_for_last_data = session.query()


id_last = session.query(func.max(Measurement.id)).all()[0][0]

station_for_last_data = session.query(Measurement.station)\
                            .filter(Measurement.id == id_last).all()[0][0]
                            
end_date_last_data = session.query(Measurement.date)\
                        .filter(Measurement.id == id_last).all()[0][0]
                        
end_date_last_data = dt.datetime.strptime(end_date_last_data, '%Y-%m-%d')

begin_date_last_data = end_date_last_data - dt.timedelta(days=365)

data_tobs = session.query(Measurement.date, Measurement.tobs)\
                .filter(and_(Measurement.station == station_for_last_data,
                              Measurement.date >= begin_date_last_data,
                              Measurement.date <= end_date_last_data,)).all()
                
data_tobs_dict = dict(data_tobs)


# Define two functions
def calc_temps_start(start_date):
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
        .filter(Measurement.date >= start_date).all()

def calc_temps_start_end(start_date, end_date):
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
        .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()