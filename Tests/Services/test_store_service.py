import unittest

from Services import StoreService
from Tests.TestEnvironment import mocked_store_repo, mocked_store_repo_with_two_stores,\
    mocked_postcodes_io_service_returns_one_geolocation


class StoreServiceTests(unittest.TestCase):
    def test_get_all_with_geolocation_returns_single_store_with_correct_data(self):

        service = StoreService(mocked_store_repo(), mocked_postcodes_io_service_returns_one_geolocation())
        stores = service.get_all_with_geolocation()

        self.assertEqual(len(stores), 1)
        self.assertEqual(stores[0]['postcode'], 'test_postcode')
        self.assertEqual(stores[0]['name'], 'test_name')
        self.assertEqual(stores[0]['geolocation']['longitude'], 1.1)
        self.assertEqual(stores[0]['geolocation']['latitude'], 2.2)

    def test_get_all_with_geolocation_removes_store_with_no_geolocation(self):

        service = StoreService(mocked_store_repo_with_two_stores(),
                               mocked_postcodes_io_service_returns_one_geolocation())
        stores = service.get_all_with_geolocation()

        self.assertEqual(len(stores), 1)
        self.assertEqual(stores[0]['postcode'], 'test_postcode')
        self.assertEqual(stores[0]['name'], 'test_name')
        self.assertEqual(stores[0]['geolocation']['longitude'], 1.1)
        self.assertEqual(stores[0]['geolocation']['latitude'], 2.2)
