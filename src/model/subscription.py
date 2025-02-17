from typing import Optional

from src.model.product_details import ProductDetails


class Subscription:
    def __init__(self, id="", barcode="", billing=None, contract=None, disclaimers=None, donorConsent=None,
                 downPayment=None, handset="", handsetPrice=0.0, handsetPriceExVat=0.0, icc="", imei="", isNewBan=False,
                 isNewSubscription=False, isNpTerminationPermitted=False, isPortingSubscription=False, isPreToPost=False,
                 isPrepaid=False, isSimCardHandout=False, legal=None, legalOwner=None, msisdn="", npAfterCommitment="",
                 npContact="", npDate="", npMsisdn="", npOperator="", offeringChangeType="", operation="", product: Optional[ProductDetails] = None,
                 resultingServices=None, services=None, simType="", user=None):
        self.id = id
        self.barcode = barcode
        self.billing = billing
        self.contract = contract
        self.disclaimers = disclaimers if disclaimers else []
        self.donorConsent = donorConsent
        self.downPayment = downPayment
        self.handset = handset
        self.handsetPrice = handsetPrice
        self.handsetPriceExVat = handsetPriceExVat
        self.icc = icc
        self.imei = imei
        self.isNewBan = isNewBan
        self.isNewSubscription = isNewSubscription
        self.isNpTerminationPermitted = isNpTerminationPermitted
        self.isPortingSubscription = isPortingSubscription
        self.isPreToPost = isPreToPost
        self.isPrepaid = isPrepaid
        self.isSimCardHandout = isSimCardHandout
        self.legal = legal
        self.legalOwner = legalOwner
        self.msisdn = msisdn
        self.npAfterCommitment = npAfterCommitment
        self.npContact = npContact
        self.npDate = npDate
        self.npMsisdn = npMsisdn
        self.npOperator = npOperator
        self.offeringChangeType = offeringChangeType
        self.operation = operation
        self.product = product
        self.resultingServices = resultingServices if resultingServices else []
        self.services = services if services else []
        self.simType = simType
        self.user = user