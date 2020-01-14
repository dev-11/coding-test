from geopy.distance import great_circle


class DistanceService:
    @staticmethod
    def get_stores_within_range(geolocation, stores, distance):
        return [s for s in stores if great_circle(geolocation, extract_geolocation_from_store(s)).miles <= distance]


def extract_geolocation_from_store(store):
    return store['geolocation']['latitude'], store['geolocation']['longitude']
