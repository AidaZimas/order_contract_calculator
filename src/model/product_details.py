class ProductDetails:
    def __init__(self, current=None, disclaimers=None, monthlyCharge=None, offeringDescriptionLong="", offeringDescriptionShort="", shortName=""):
        self.current = current if current else CurrentProduct()
        self.disclaimers = disclaimers if disclaimers else []
        self.monthlyCharge = monthlyCharge if monthlyCharge else MonthlyCharge()
        self.offeringDescriptionLong = offeringDescriptionLong
        self.offeringDescriptionShort = offeringDescriptionShort
        self.shortName = shortName