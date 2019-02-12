import json

from pathlib import Path

from ucrmapiwrap.clients import UCRMClients
from ucrmapiwrap.services import UCRMServices


def update_client_structs():
    client = UCRMClients(params={'offset': 1})._clients_list[0]
    client_struct = {k: None for k in client}
    curdir = Path(__file__).parent
    file_name = f'{curdir}\\tests\\call_structs\\client.json'
    with open(file_name, 'w') as file:
        json.dump(client_struct, file)


def update_service_structs():
    service = UCRMServices(params={'offset': 1})._services_list[0]
    service_struct = {k: None for k in service}
    curdir = Path(__file__).parent
    file_name = f'{curdir}\\tests\\call_structs\\service.json'
    with open(file_name, 'w') as file:
        json.dump(service_struct, file)
