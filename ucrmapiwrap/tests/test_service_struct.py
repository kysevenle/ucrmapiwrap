import json
import pytest

from pathlib import Path

from ucrmapiwrap.services import UCRMServices


@pytest.fixture
def service_from_api():
    service = UCRMServices(params={'limit': 1})[0]
    return service


@pytest.fixture
def service_from_json():
    cur_dir = Path(__file__).parent
    file_name = f'{cur_dir}\\call_structs\\service.json'
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


def test_service_structure(service_from_api, service_from_json):
    assert vars(service_from_api).keys() == service_from_json.keys()
