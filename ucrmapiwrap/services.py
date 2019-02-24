import requests

from ucrmapiwrap.config_reader import config
from ucrmapiwrap.service import UCRMService


class UCRMServices:
    def __init__(self, params=None):
        self.url = config.BASE_URL + 'clients/services'
        self.headers = {'Content-Type': 'application/json',
                        'x-Auth-App-Key': config.WRITE_KEY}
        self._services_list = []
        self.errors = {}

        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            self._services_list = [UCRMService(**service) for service in response.json()]
        else:
            self.errors = response.json()

    def __iter__(self):
        for service in self._services_list:
            yield UCRMService(**service)

    def __len__(self):
        return len(self._services_list)

    def __getitem__(self, position):
        return self._services_list[position]
