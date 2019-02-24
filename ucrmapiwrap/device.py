from ucrmapiwrap.base import UCRMBase
from ucrmapiwrap.config_reader import config


class UCRMDevice(UCRMBase):
    url = config.BASE_URL + 'devices'

    def __init__(self, *, id, name, siteId, vendorId, modelName, parentIds, notes,
                 loginUsername, sshPort, snmpCommunity, osVersion, isGateway,
                 isSuspendEnabled, sendPingNotifications, pingNotificationUserId,
                 createSignalStatistics):
        self.id = id
        self.name = name
        self.siteId = siteId
        self.vendorId = vendorId
        self.modelName = modelName
        self.parentIds = parentIds
        self.notes = notes
        self.loginUsername = loginUsername
        self.sshPort = sshPort
        self.snmpCommunity = snmpCommunity
        self.osVersion = osVersion
        self.isGateway = isGateway
        self.isSuspendEnabled = isSuspendEnabled
        self.sendPingNotifications = sendPingNotifications
        self.pingNotificationUserId = pingNotificationUserId
        self.createSignalStatistics = createSignalStatistics

    def __repr__(self):
        return str(vars(self))
