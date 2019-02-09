import requests

from ucrmapiwrap.config_reader import config


class Services:
    def __init__(self):
        self.url = config.BASE_URL + 'clients/services'
        self.headers = {'Content-Type': 'application/json',
                        'x-Auth-App-Key': config.WRITE_KEY}
        self.batch = []
        self.errors = {}

    def get_services_list(self, params=None):
        self.batch = requests.get(self.url, headers=self.headers, params=params).json()

    def get_service_by_id(self, id):
        url = f'{self.url}/{id}'
        return requests.get(url, headers=self.headers)

    def __iter__(self):
        for service in self.batch:
            yield service

    def __len__(self):
        return len(self.batch)


params = {'statuses[]': 3}
services = Services()
services.get_services_list(params)
print(len(services))
