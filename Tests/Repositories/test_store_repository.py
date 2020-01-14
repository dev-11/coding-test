import unittest
from Repositories import StoreRepository


class StoreRepositoryTests(unittest.TestCase):
    def test_empty_repo_returns_empty_list(self):
        json_file = 'Tests/TestEnvironment/empty.json'
        repo = StoreRepository(json_file)
        stores = repo.get_all()
        self.assertFalse(stores)

    def test_repo_returns_correct_single_item(self):
        json_file = 'Tests/TestEnvironment/single.json'
        repo = StoreRepository(json_file)
        stores = repo.get_all()
        self.assertEqual(len(stores), 1)

        self.assertEqual(stores[0]['name'], 'St_Albans')
        self.assertEqual(stores[0]['postcode'], 'AL1 2RJ')

    def test_repo_returns_correct_multiple_items(self):
        json_file = 'Tests/TestEnvironment/several_items.json'
        repo = StoreRepository(json_file)
        stores = repo.get_all()
        self.assertEqual(len(stores), 2)

        self.assertEqual(stores[0]['name'], 'St_Albans')
        self.assertEqual(stores[0]['postcode'], 'AL1 2RJ')

        self.assertEqual(stores[1]['name'], 'Hatfield')
        self.assertEqual(stores[1]['postcode'], 'AL9 5JP')
