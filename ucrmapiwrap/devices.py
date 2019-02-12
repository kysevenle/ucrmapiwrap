import requests

from ucrmapiwrap.config_reader import config
from ucrmapiwrap.device import UCRMDevice


class UCRMDevices:
    def __init__(self):
        self.url = config.BASE_URL + 'devices'
        self.headers = {'Content-Type': 'application/json',
                        'x-Auth-App-Key': config.WRITE_KEY}
        self._devices_list = []
        self.errors = {}

        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self._devices_list = response.json()
        else:
            self.errors = response.json()

        def __iter__(self):
            for device in self._devices_list:
                yield UCRMDevice(**device)

        def __len__(self):
            return len(self._devices_list)
