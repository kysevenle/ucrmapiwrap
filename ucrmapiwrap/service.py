class Service():
    def __init__(self, *, id, clientId, status, name, street1, street2, city, countryId,
                 stateId, zipCode, note, addressGpsLat, addressGpsLon, servicePlanId,
                 servicePlanPeriodId, price, hasIndividualPrice, totalPrice, currencyCode,
                 invoiceLabel, contractId, contractLengthType,
                 minimumContractLengthMonths, activeFrom, activeTo, contractEndDate,
                 discountType, discountValue, discountInvoiceLabel, discountFrom,
                 discountTo, tax1Id, tax2Id, tax3Id, invoicingStart, invoicingPeriodType,
                 invoicingPeriodStartDay, nextInvoicingDayAdjustment,
                 invoicingProratedSeparately, invoicingSeparately,
                 sendEmailsAutomatically, useCreditAutomatically, servicePlanName,
                 servicePlanPrice, servicePlanPeriod, downloadSpeed, uploadSpeed,
                 ipRanges, hasOutage, fccBlockId, lastInvoicedDate):
        self.id = id
        self.clientId = clientId
        self.status = status
        self.name = name
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.countryId = countryId
        self.stateId = stateId
        self.zipCode = zipCode
        self.note = note
        self.addressGpsLat = addressGpsLat
        self.addressGpsLon = addressGpsLon
        self.servicePlanId = servicePlanId
        self.servicePlanPeriodId = servicePlanPeriodId
        self.price = price
        self.hasIndividualPrice = hasIndividualPrice
        self.totalPrice = totalPrice
        self.currencyCode = currencyCode
        self.invoiceLabel = invoiceLabel
        self.contractId = contractId
        self.contractLengthType = contractLengthType
        self.minimumContractLengthMonths = minimumContractLengthMonths
        self.activeFrom = activeFrom
        self.activeTo = activeTo
        self.contractEndDate = contractEndDate
        self.discountType = discountType
        self.discountValue = discountValue
        self.discountInvoiceLabel = discountInvoiceLabel
        self.discountFrom = discountFrom
        self.discountTo = discountTo
        self.tax1Id = tax1Id
        self.tax2Id = tax2Id
        self.tax3Id = tax3Id
        self.invoicingStart = invoicingStart
        self.invoicingPeriodType = invoicingPeriodType
        self.invoicingPeriodStartDay = invoicingPeriodStartDay
        self.nextInvoicingDayAdjustment = nextInvoicingDayAdjustment
        self.invoicingProratedSeparately = invoicingProratedSeparately
        self.invoicingSeparately = invoicingSeparately
        self.sendEmailsAutomatically = sendEmailsAutomatically
        self.useCreditAutomatically = useCreditAutomatically
        self.servicePlanName = servicePlanName
        self.servicePlanPrice = servicePlanPrice
        self.servicePlanPeriod = servicePlanPeriod
        self.downloadSpeed = downloadSpeed
        self.uploadSpeed = uploadSpeed
        self.ipRanges = ipRanges
        self.hasOutage = hasOutage
        self.fccBlockId = fccBlockId
        self.lastInvoicedDate = lastInvoicedDate
