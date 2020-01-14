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
