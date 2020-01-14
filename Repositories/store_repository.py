import json


class StoreRepository:
    def __init__(self, json_file):
        self._json_file = json_file

    def get_all(self):
        with open(self._json_file, 'r') as read_file:
            return json.load(read_file)