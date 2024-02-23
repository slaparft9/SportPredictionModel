# This file handles the api request logic for the espn api (and possible any api)


import requests


class ESPNAPI:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_data(self):
        response = requests.get(self.endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None
