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

    @property
    def payload(self):
        payload = {'interfaceId': self.interfaceId,
                   'vendorId': self.vendorId,
                   'ipRange': self.ipRange,
                   'macAddress': self.macAddress,
                   'loginUsername': self.loginUsername,
                   'loginPassword': self.loginPassword,
                   'sshPort': self.sshPort,
                   'sendPingNotifications': self.sendPingNotifications,
                   'pingNotificationUserId': self.pingNotificationUserId,
                   'createPingStatistics': self.createPingStatistics,
                   'createSignalStatistics': self.createSignalStatistics,
                   'qosEnabled': self.qosEnabled,
                   'qosDeviceIds': self.qosDeviceIds}
        return payload

    def __repr__(self):
        return str(vars(self))
