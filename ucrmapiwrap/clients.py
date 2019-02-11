import requests

from ucrmapiwrap.client import Client
from ucrmapiwrap.config_reader import config


class UCRMClients:
    def __init__(self, params=None):
        self.url = config.BASE_URL + 'clients'
        self.headers = {'Content-Type': 'application/json',
                        'x-Auth-App-Key': config.WRITE_KEY}
        self._clients_list = []
        self.errors = {}

        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            self._clients_list = response.json()
        else:
            self.errors = response.json()

    def __iter__(self):
        for client in self._clients_list:
            yield Client(**client)

    def __len__(self):
        return len(self._clients_list)
