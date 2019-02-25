from ucrmapiwrap.services import UCRMServices
from ucrmapiwrap.service_devices import UCRMServiceDevices


def remove_signal_stats():
    services = UCRMServices(params={'statuses[]': [1, 3]})
    service_devices = [UCRMServiceDevices(service.id) for service in services]
    service_devices_with_ss = [service_device for service in service_devices for
                               service_device in service
                               if service_device.createSignalStatistics is True]
    for service_device in service_devices_with_ss:
        service_device.createSignalStatistics = False
        service_device.patch()
