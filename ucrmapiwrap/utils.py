import json

from pathlib import Path

from ucrmapiwrap.clients import UCRMClients
from ucrmapiwrap.devices import UCRMDevices
from ucrmapiwrap.service_devices import UCRMServiceDevices
from ucrmapiwrap.services import UCRMServices


def update_client_structs():
    client = UCRMClients(params={'limit': 1})[0]
    client_struct = {k: None for k in vars(client)}
    curdir = Path(__file__).parent
    file_name = f'{curdir}\\tests\\call_structs\\client.json'
    with open(file_name, 'w') as file:
        json.dump(client_struct, file)


def update_service_structs():
    service = UCRMServices(params={'limit': 1})[0]
    service_struct = {k: None for k in vars(service)}
    curdir = Path(__file__).parent
    file_name = f'{curdir}\\tests\\call_structs\\service.json'
    with open(file_name, 'w') as file:
        json.dump(service_struct, file)


def update_device_structs():
    device = UCRMDevices()[0]
    device_struct = {k: None for k in vars(device)}
    curdir = Path(__file__).parent
    file_name = f'{curdir}\\tests\\call_structs\\device.json'
    with open(file_name, 'w') as file:
        json.dump(device_struct, file)


def update_service_device_structs():
    service = UCRMServices(params={'limit': 1})[0]
    service_device = UCRMServiceDevices(service.id)
    service_device_struct = {k: None for k in vars(service_device)}
    curdir = Path(__file__).parent
    file_name = f'{curdir}\\tests\\call_structs\\service_device.json'
    with open(file_name, 'w') as file:
        json.dump(service_device_struct, file)
