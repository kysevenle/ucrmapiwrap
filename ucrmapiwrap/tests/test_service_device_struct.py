import json
import pytest

from pathlib import Path

from ucrmapiwrap.services import UCRMServices
from ucrmapiwrap.service_devices import UCRMServiceDevices


@pytest.fixture
def service_device_from_api():
    service = UCRMServices(params={'limit': 1})[0]
    service_device = UCRMServiceDevices(service.id)[0]
    return service_device


@pytest.fixture
def service_device_from_json():
    cur_dir = Path(__file__).parent
    file_name = f'{cur_dir}\\call_structs\\service_device.json'
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


def test_service_device_structure(service_device_from_api, service_device_from_json):
    assert vars(service_device_from_api).keys() == service_device_from_json.keys()
