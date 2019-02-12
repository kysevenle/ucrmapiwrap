import json
import pytest

from pathlib import Path

from ucrmapiwrap.clients import UCRMClients


@pytest.fixture
def client_from_api():
    client = UCRMClients(params={'limit': 1})._clients_list[0]
    return [*client]


@pytest.fixture
def client_from_json():
    cur_dir = Path(__file__).parent
    file_name = f'{cur_dir}\\call_structs\\client.json'
    with open(file_name, 'r') as file:
        data = json.load(file)
    return [*data]


def test_client_structure(client_from_api, client_from_json):
    assert client_from_api == client_from_json
