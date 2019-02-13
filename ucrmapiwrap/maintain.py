from ucrmapiwrap.services import UCRMServices
from ucrmapiwrap.service_device import UCRMServiceDevice
from ucrmapiwrap.service_devices import UCRMServiceDevices


def remove_signal_stats():
    services = UCRMServices(params={'statuses[]': [1, 3]})
    service_devices = [UCRMServiceDevice(**service_device) for service in services
                       for service_device
                       in UCRMServiceDevices(service.id)._service_devices_list
                       if service_device['createSignalStatistics'] is True]
    for service_device in service_devices:
        print(service_device.id)
