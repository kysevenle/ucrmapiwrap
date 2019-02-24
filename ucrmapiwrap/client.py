import requests

from ucrmapiwrap.config_reader import config


class UCRMClient():
    url = config.BASE_URL + 'clients'
    headers = {'Content-Type': 'application/json',
               'x-Auth-App-Key': config.WRITE_KEY}

    def __init__(self, *, id, userIdent, previousIsp, isLead, clientType, companyName,
                 companyRegistrationNumber, companyTaxId, companyWebsite, street1,
                 street2, city, countryId, stateId, zipCode, invoiceStreet1,
                 invoiceStreet2, invoiceCity, invoiceStateId, invoiceCountryId,
                 invoiceZipCode, invoiceAddressSameAsContact, note, sendInvoiceByPost,
                 invoiceMaturityDays, stopServiceDue, stopServiceDueDays, organizationId,
                 tax1Id, tax2Id, tax3Id, registrationDate, companyContactFirstName,
                 companyContactLastName, isActive, firstName, lastName, username,
                 contacts, attributes, accountBalance, accountCredit, accountOutstanding,
                 currencyCode, organizationName, bankAccounts, tags,
                 invitationEmailSentDate, avatarColor, addressGpsLat, addressGpsLon,
                 isArchived):
        self.id = id
        self.userIdent = userIdent
        self.previousIsp = previousIsp
        self.isLead = isLead
        self.clientType = clientType
        self.companyName = companyName
        self.companyRegistrationNumber = companyRegistrationNumber
        self.companyTaxId = companyTaxId
        self.companyWebsite = companyWebsite
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.countryId = countryId
        self.stateId = stateId
        self.zipCode = zipCode
        self.invoiceStreet1 = invoiceStreet1
        self.invoiceStreet2 = invoiceStreet2
        self.invoiceCity = invoiceCity
        self.invoiceStateId = invoiceStateId
        self.invoiceCountryId = invoiceCountryId
        self.invoiceZipCode = invoiceZipCode
        self.invoiceAddressSameAsContact = invoiceAddressSameAsContact
        self.note = note
        self.sendInvoiceByPost = sendInvoiceByPost
        self.invoiceMaturityDays = invoiceMaturityDays
        self.stopServiceDue = stopServiceDue
        self.stopServiceDueDays = stopServiceDueDays
        self.organizationId = organizationId
        self.tax1Id = tax1Id
        self.tax2Id = tax2Id
        self.tax3Id = tax3Id
        self.registrationDate = registrationDate
        self.companyContactFirstName = companyContactFirstName
        self.companyContactLastName = companyContactLastName
        self.isActive = isActive
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.contacts = contacts
        self.attributes = attributes
        self.accountBalance = accountBalance
        self.accountCredit = accountCredit
        self.accountOutstanding = accountOutstanding
        self.currencyCode = currencyCode
        self.organizationName = organizationName
        self.bankAccounts = bankAccounts
        self.tags = tags
        self.invitationEmailSentDate = invitationEmailSentDate
        self.avatarColor = avatarColor
        self.addressGpsLat = addressGpsLat
        self.addressGpsLon = addressGpsLon
        self.isArchived = isArchived

    @classmethod
    def from_api(cls, id):
        url = f'{cls.url}/{id}'
        response = requests.get(url, headers=cls.headers)
        if response.status_code == 200:
            return cls(**response.json())

    def __repr__(self):
        return str(vars(self))
