import requests

from ucrmapiwrap.config_reader import config
from ucrmapiwrap.service_device import UCRMServiceDevice


class UCRMServiceDevices:
    def __init__(self, service_id):
        self.url = f'{config.BASE_URL}clients/services/{service_id}/service-devices'
        self.headers = {'Content-Type': 'application/json',
                        'x-Auth-App-Key': config.WRITE_KEY}
        self._service_devices_list = []
        self.errors = {}

        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self._service_devices_list = [UCRMServiceDevice(**service_device) for
                                          service_device in response.json()]
        else:
            self.errors = response.json()

    def __iter__(self):
        for service_device in self._service_devices_list:
            yield service_device

    def __len__(self):
        return len(self._service_devices_list)

    def __getitem__(self, position):
        return self._service_devices_list[position]
