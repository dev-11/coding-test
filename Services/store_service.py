class StoreService:

    def __init__(self, store_repository, postcode_service):
        self._store_repo = store_repository
        self._postcode_service = postcode_service

    def get_all_with_geolocation(self):
        stores = self._store_repo.get_all()
        postcodes = [store['postcode'] for store in stores]
        geolocations = self._postcode_service.get_geolocations(postcodes)

        for postcode in postcodes:
            store = next(store for store in stores if store['postcode'] == postcode)
            store['geolocation'] = geolocations[postcode] if postcode in geolocations else None

        return [store for store in stores if store['geolocation'] is not None]

