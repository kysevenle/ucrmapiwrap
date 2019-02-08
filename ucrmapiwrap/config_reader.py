import json
from collections import namedtuple
from pathlib import Path


Config = namedtuple('Config', ['BASE_URL', 'WRITE_KEY', ])


def read_config():

    curdir = Path(__file__).parent
    config_path = f'{curdir}\\config.json'

    with open(config_path, 'r') as file:
        config_dict = json.load(file)
        config = Config(config_dict['baseUrl'], config_dict['writeKey'])
        return config


config = read_config()
