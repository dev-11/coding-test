from flask import Flask, render_template, jsonify, request
from geopy.distance import great_circle

from Repositories import StoreRepository
from ExternalServices import PostcodesIoService

from config import STORES_TEMPLATE, API_ENDPOINT, JSON_FILE, PORT_NUMBER

app = Flask(__name__)


@app.route('/')
def get_stores():

    store_repo = StoreRepository(JSON_FILE)
    stores = store_repo.get_all()

    postcodes = [store['postcode'] for store in stores]

    postcode_service = PostcodesIoService(API_ENDPOINT)
    geolocations = postcode_service.get_geolocations(postcodes)

    for postcode in postcodes:
        store = next(store for store in stores if store['postcode'] == postcode)
        store['geolocation'] = geolocations[postcode] if postcode in geolocations else None

    return render_template(STORES_TEMPLATE, stores=stores)


@app.route('/nearme/<string:postcode>/<int:distance>')
def near_me(postcode, distance):

    postcode_service = PostcodesIoService(API_ENDPOINT)
    postcode_geolocation = postcode_service.get_geolocation(postcode)

    store_repo = StoreRepository(JSON_FILE)
    stores = store_repo.get_all()

    postcodes = [store['postcode'] for store in stores]
    geolocations = postcode_service.get_geolocations(postcodes)

    for postcode in postcodes:
        store = next(store for store in stores if store['postcode'] == postcode)
        store['geolocation'] = geolocations[postcode] if postcode in geolocations else None

    given_location = (postcode_geolocation['latitude'], postcode_geolocation['longitude'])

    stores_near = []

    for store in stores:
        print(store)
        if store['geolocation'] is not None:
            store_location = (store['geolocation']['latitude'], store['geolocation']['longitude'])
            if great_circle(given_location, store_location).miles < distance:
                stores_near.append(store)

    return jsonify(stores_near)


if __name__ == '__main__':
    app.config.from_object('config')
    app.run(port=PORT_NUMBER)

