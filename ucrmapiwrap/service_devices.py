import requests

from ucrmapiwrap.config_reader import config
from ucrmapiwrap.service_device import UCRMServiceDevice


class UCRMServiceDevices:
    def __init__(self, id):
        self.url = f'{config.BASE_URL}clients/services/{id}/service-devices'
        self.headers = {'Content-Type': 'application/json',
                        'x-Auth-App-Key': config.WRITE_KEY}
        self._service_devices_list = []
        self.errors = {}

        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self._service_devices_list = response.json()
        else:
            self.errors = response.json()

        def _iter__(self):
            for service_device in self._service_devices_list:
                yield UCRMServiceDevice(**service_device)
