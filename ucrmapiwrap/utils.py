import json

from pathlib import Path

from ucrmapiwrap.clients import UCRMClients


def update_client_structs():
    client = UCRMClients()._clients_list[0]
    client_struct = {k: None for k in client}
    curdir = Path(__file__).parent
    file_name = f'{curdir}\\tests\\call_structs\\client.json'
    with open(file_name, 'w') as file:
        json.dump(client_struct, file)
