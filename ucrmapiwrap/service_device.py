import requests

from ucrmapiwrap.config_reader import config


class UCRMServiceDevice:
    url = config.BASE_URL + 'clients/services/service-devices'
    headers = {'Content-Type': 'application/json',
               'x-Auth-App-Key': config.WRITE_KEY}

    def __init__(self, *, interfaceId, vendorId, ipRange, macAddress, loginUsername,
                 sshPort, sendPingNotifications, pingNotificationUserId,
                 createPingStatistics, createSignalStatistics, qosEnabled, qosDeviceIds,
                 id, serviceId, loginPassword):
        self.interfaceId = interfaceId
        self.vendorId = vendorId
        self.ipRange = ipRange
        self.macAddress = macAddress
        self.loginUsername = loginUsername
        self.sshPort = sshPort
        self.sendPingNotifications = sendPingNotifications
        self.pingNotificationUserId = pingNotificationUserId
        self.createPingStatistics = createPingStatistics
        self.createSignalStatistics = createSignalStatistics
        self.qosEnabled = qosEnabled
        self.qosDeviceIds = qosDeviceIds
        self.id = id
        self.serviceId = serviceId
        self.loginPassword = loginPassword

    @classmethod
    def from_api(cls, id):
        url = f'{cls.url}/{id}'
        response = requests.get(url, headers=cls.headers)
        if response.status_code == 200:
            return cls(**response.json())
