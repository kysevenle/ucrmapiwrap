import requests

from ucrmapiwrap.config_reader import config


class Services:
    def __init__(self):
        self.url = config.BASE_URL + 'clients/services'
        self.headers = {'Content-Type': 'application/json',
                        'x-Auth-App-Key': config.WRITE_KEY}

    def get_services_list(self, params=None):
        return requests.get(self.url, headers=self.headers, params=params)

    def get_service_by_id(self, id):
        url = f'{self.url}/{id}'
        return requests.get(url, headers=self.headers)
