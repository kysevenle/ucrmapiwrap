import requests


class UCRMBase:

    @classmethod
    def get(cls, id):
        url = f'{cls.url}/{id}'
        response = requests.get(url, headers=cls.headers)
        if response.status_code == 200:
            return cls(**response.json())
