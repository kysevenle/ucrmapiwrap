import requests

from ucrmapiwrap.config_reader import config


class UCRMBase:
    headers = {'Content-Type': 'application/json',
               'x-Auth-App-Key': config.WRITE_KEY}

    @classmethod
    def get(cls, id):
        url = f'{cls.url}/{id}'
        response = requests.get(url, headers=cls.headers)
        if response.status_code == 200:
            return cls(**response.json())
