import requests


class PostcodesIoService:
    def __init__(self, api_endpoint):
        self._api_endpoint = api_endpoint

    def get_geolocations(self, postcodes):
        api_post = requests.post(url=self._api_endpoint, json={'postcodes': postcodes})
        api_result = api_post.json()

        result = {}

        for postcode in postcodes:
            postcode_api_result = next(api_result['result'] for api_result in api_result['result']
                                       if api_result['query'] == postcode)

            if postcode_api_result:
                result[postcode] = {
                    'latitude': postcode_api_result['latitude'],
                    'longitude': postcode_api_result['longitude']
                }

        return result

    def get_geolocation(self, postcode):
        api_get = requests.get(url=self._api_endpoint+postcode)
        api_result = api_get.json()
        postcode_api_result = api_result['result']

        return {
                'latitude': postcode_api_result['latitude'],
                'longitude': postcode_api_result['longitude']
        }
