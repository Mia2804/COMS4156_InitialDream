from flask import Blueprint
from flask import Flask, jsonify
from flask_googlemaps import GoogleMaps
import requests

app = Flask(__name__)

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyCV6i7A51OYP5oeqzi4d1vpl05wSFRLtcc"

# Initialize the extension
GoogleMaps(app)

import googlemaps

API_KEY = "AIzaSyCV6i7A51OYP5oeqzi4d1vpl05wSFRLtcc"


bp = Blueprint('locate', __name__,url_prefix='/locate')

@bp.route('/locate', methods=('GET', 'POST'))
def locate():
    gmaps = googlemaps.Client(key=API_KEY)
    locations = gmaps.geolocate()
    latitude = locations['location']['lat']
    longitude = locations['location']['lng']

    # api-endpoint
    URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"
    # API key
    api_key = '0Kyf34G-M29rR0x44xq-BX02bxhQwsXIhCOmEFY7Eh0'
    # Defining a params dictionary for the parameters to be sent to the API
    PARAMS = {
        'at': '{},{}'.format(latitude, longitude),
        'apikey': api_key
    }
    # Sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # Extracting data in json format
    data = r.json()

    # Taking out title from JSON
    address = data['items'][0]['title']

    return address

