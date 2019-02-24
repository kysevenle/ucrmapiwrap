import json
import pytest

from pathlib import Path

from ucrmapiwrap.devices import UCRMDevices


@pytest.fixture
def device_from_api():
    device = UCRMDevices()[0]
    return device


@pytest.fixture
def device_from_json():
    cur_dir = Path(__file__).parent
    file_name = f'{cur_dir}\\call_structs\\device.json'
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


def test_client_structure(device_from_api, device_from_json):
    assert vars(device_from_api).keys() == device_from_json.keys()
