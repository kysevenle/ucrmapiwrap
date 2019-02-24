from ucrmapiwrap.base import UCRMBase
from ucrmapiwrap.config_reader import config


class UCRMServiceDevice(UCRMBase):
    url = config.BASE_URL + 'clients/services/service-devices'

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

    def __repr__(self):
        return str(vars(self))
