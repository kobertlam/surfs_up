# import the dependencies for datetime, NumPy, and Pandas
import datetime as dt
import numpy as np
import pandas as pd
# Import dependencies for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Import dependencies for Flask
from flask import Flask, jsonify

######################
# Setup the Database
######################

# Setup the Database, allow you to access and query the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# Produce a declarative automap base.
Base = automap_base()

# Reflect the tables into SQLAlchemy
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes referring to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our Database
session = Session(engine)

######################
# Setup Flask
######################

# Create a new Flask application instance called 'app'
app = Flask(__name__)

# Create Flask routes

# Define the welcome route (the "root")
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end<br>
    ''')
# Define the Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   # convert the list into dictionary
   precip = {date: prcp for date, prcp in precipitation}
   # Jsonify the dictionary
   return jsonify(precip)
# Define the Stations Route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    # use np.ravel() to unraveling the results into a one-dimensional array, and then convert the array into a list
    stations = list(np.ravel(results))
    # Jsonify the list and return it as JSON
    # use 'stations=stations' to format the list into JSON
    return jsonify(stations=stations)
# Define the Temperature Route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # use np.ravel() to unraveling the results into a one-dimensional array, and then convert the array into a list
    temps = list(np.ravel(results))
    # Jsonify the list and return it as JSON
    return jsonify(temps=temps)
# Define the Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
    
