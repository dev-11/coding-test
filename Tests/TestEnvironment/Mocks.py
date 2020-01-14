from unittest.mock import Mock

from Repositories import StoreRepository
from ExternalServices import PostcodesIoService


def mocked_store_repo():
    repo = StoreRepository(None)
    repo.get_all = Mock(name='get_all')
    repo.get_all.return_value = [{
        'name': 'test_name',
        'postcode': 'test_postcode'
    }]
    return repo


def mocked_store_repo_with_two_stores():
    repo = StoreRepository(None)
    repo.get_all = Mock(name='get_all')
    repo.get_all.return_value = [{
        'name': 'test_name',
        'postcode': 'test_postcode'
    },
        {
            'name': 'test_name2',
            'postcode': 'test_postcode2'
        }]
    return repo


def mocked_postcodes_io_service_returns_one_geolocation():
    postcode_service = PostcodesIoService(None)
    postcode_service.get_geolocations = Mock(name='get_geolocations')
    postcode_service.get_geolocations.return_value = {
        "test_postcode": {
            "longitude": 1.1,
            "latitude": 2.2
        }
    }
    return postcode_service


def get_test_stores():
    return [
        {
            "geolocation": {
                "latitude": 51.555701,
                "longitude": -0.390474
            },
            "name": "Ruislip",
            "postcode": "HA4 0LN"
        },
        {
            "geolocation": {
                "latitude": 51.543913,
                "longitude": -0.13693
            },
            "name": "Camden",
            "postcode": "NW1 9EX"
        },
        {
            "geolocation": {
                "latitude": 51.580711,
                "longitude": -0.245101
            },
            "name": "Hendon",
            "postcode": "NW9 7TH"
        },
        {
            "geolocation": {
                "latitude": 51.470125,
                "longitude": -0.176813
            },
            "name": "Battersea",
            "postcode": "SW11 3RX"
        },
        {
            "geolocation": {
                "latitude": 51.429853,
                "longitude": -0.185911
            },
            "name": "Wimbledon",
            "postcode": "SW17 0BW"
        },
        {
            "geolocation": {
                "latitude": 51.405065,
                "longitude": -0.238117
            },
            "name": "New_Malden",
            "postcode": "SW20 0JQ"
        },
        {
            "geolocation": {
                "latitude": 51.442892,
                "longitude": -0.412804
            },
            "name": "Feltham",
            "postcode": "TW13 4EX"
        },
        {
            "geolocation": {
                "latitude": 51.482172,
                "longitude": -0.314343
            },
            "name": "Brentford",
            "postcode": "TW8 8JW"
        },
        {
            "geolocation": {
                "latitude": 51.463437,
                "longitude": -0.288602
            },
            "name": "Richmond",
            "postcode": "TW9 1YB"
        },
        {
            "geolocation": {
                "latitude": 51.51461,
                "longitude": -0.397889
            },
            "name": "Hayes",
            "postcode": "UB4 0TU"
        },
        {
            "geolocation": {
                "latitude": 51.541836,
                "longitude": -0.34005
            },
            "name": "Greenford",
            "postcode": "UB6 0UW"
        }
    ]
