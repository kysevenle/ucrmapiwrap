import requests

from ucrmapiwrap.config_reader import config


class UCRMDevice:
    url = config.BASE_URL + 'devices'
    headers = {'Content-Type': 'application/json',
               'x-Auth-App-Key': config.WRITE_KEY}

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

    @classmethod
    def from_api(cls, id):
        url = f'{cls.url}/{id}'
        response = requests.get(url, headers=cls.headers)
        if response.status_code == 200:
            return cls(**response.json())
