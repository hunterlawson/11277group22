from flask import Flask
from pymongo import MongoClient
from os import environ

app = Flask(__name__)

# Set the Flask secret key, which is used for things like authenticating
# the forms and for user authentication
app.config['SECRET_KEY'] = '123'

MONGO_URI = environ.get('SUNSPOT_MONGO_URI')
if MONGO_URI == None:
    MONGO_URI = 'mongodb://localhost:27017'
db_client = MongoClient(MONGO_URI) # Connect to the local server
db = db_client.sunspot # Open the SunSpot database

from sunspot import views