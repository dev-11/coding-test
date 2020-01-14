import unittest

from Services import DistanceService
from Tests.TestEnvironment import get_test_stores


class DistanceServiceTests(unittest.TestCase):
    def test_get_stores_within_range_returns_every_store_in_one_mile_range(self):

        a = [51.460903, -0.301702]
        stores = get_test_stores()

        service = DistanceService()
        result = service.get_stores_within_range(a, stores, 1)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['geolocation']['latitude'], 51.463437)
        self.assertEqual(result[0]['geolocation']['longitude'], -0.288602)
        self.assertEqual(result[0]['name'], 'Richmond')
        self.assertEqual(result[0]['postcode'], 'TW9 1YB')

    def test_get_stores_within_range_returns_every_store_in_five_miles_range(self):

        a = [51.460903, -0.301702]
        stores = get_test_stores()

        service = DistanceService()
        result = service.get_stores_within_range(a, stores, 5)

        self.assertEqual(len(result), 4)

        self.assertEqual(result[0]['geolocation']['latitude'], 51.405065)
        self.assertEqual(result[0]['geolocation']['longitude'], -0.238117)
        self.assertEqual(result[0]['name'], 'New_Malden')
        self.assertEqual(result[0]['postcode'], 'SW20 0JQ')

        self.assertEqual(result[1]['geolocation']['latitude'], 51.442892)
        self.assertEqual(result[1]['geolocation']['longitude'], -0.412804)
        self.assertEqual(result[1]['name'], 'Feltham')
        self.assertEqual(result[1]['postcode'], 'TW13 4EX')

        self.assertEqual(result[2]['geolocation']['latitude'], 51.482172)
        self.assertEqual(result[2]['geolocation']['longitude'], -0.314343)
        self.assertEqual(result[2]['name'], 'Brentford')
        self.assertEqual(result[2]['postcode'], 'TW8 8JW')

        self.assertEqual(result[3]['geolocation']['latitude'], 51.463437)
        self.assertEqual(result[3]['geolocation']['longitude'], -0.288602)
        self.assertEqual(result[3]['name'], 'Richmond')
        self.assertEqual(result[3]['postcode'], 'TW9 1YB')
