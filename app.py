from flask import Flask, render_template, jsonify, request

from Repositories import StoreRepository
from ExternalServices import PostcodesIoService
from Services import StoreService, DistanceService

from config import STORES_TEMPLATE, API_ENDPOINT, JSON_FILE, PORT_NUMBER

app = Flask(__name__)


@app.route('/')
def get_stores():
    store_service = StoreService(StoreRepository(JSON_FILE), PostcodesIoService(API_ENDPOINT))
    stores = store_service.get_all_with_geolocation()

    return render_template(STORES_TEMPLATE, stores=stores)


@app.route('/nearme/<string:postcode>/<int:distance>')
def near_me(postcode, distance):
    postcode_service = PostcodesIoService(API_ENDPOINT)
    postcode_geolocation = postcode_service.get_geolocation(postcode)

    store_service = StoreService(StoreRepository(JSON_FILE), PostcodesIoService(API_ENDPOINT))
    stores = store_service.get_all_with_geolocation()

    given_location = postcode_geolocation['latitude'], postcode_geolocation['longitude']

    stores_near = DistanceService.get_stores_within_range(given_location, stores, distance)

    return jsonify(stores_near)


if __name__ == '__main__':
    app.config.from_object('config')
    app.run(port=PORT_NUMBER)

