import json
import pytest

from pathlib import Path

from ucrmapiwrap.devices import UCRMDevices


@pytest.fixture
def device_from_api():
    client = UCRMDevices()._devices_list[0]
    return [*client]


@pytest.fixture
def device_from_json():
    cur_dir = Path(__file__).parent
    file_name = f'{cur_dir}\\call_structs\\device.json'
    with open(file_name, 'r') as file:
        data = json.load(file)
    return [*data]


def test_client_structure(device_from_api, device_from_json):
    assert device_from_api == device_from_json
