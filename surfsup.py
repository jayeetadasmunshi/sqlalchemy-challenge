##############################################
# Designing a Flask API
##############################################
# Importing the required libraries
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Importing Flask and jsonify
from flask import Flask, jsonify
from flask import render_template

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo = False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Mapping measurement class
Measurement = Base.classes.measurement
# Mapping station class
Station = Base.classes.station

#################################################
# Querying dates in the database
#################################################
# Create our session (link) from Python to the DB
session = Session(bind=engine)
# Let's count the total dates we have
total_dates = session.query(func.count(Measurement.date)).first()
# Let's find the earliest date
earliest_date = session.query(Measurement.date).order_by(Measurement.date).first()
# Let's find the latest date
latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
# Let's find date 12 months before the latest day
query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
# Closing session link
session.close()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Define what to do when a user hits the index route
@app.route("/")
def home():
    """List all available api routes."""
    return 
