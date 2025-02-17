class Service:
    def __init__(self, action="", category="", characteristics=None, classification="", code="", customerRelevant=False, flexibleSwitch=None, insurance=None, insuranceClass="", isSecretNumber=False, monthlyCharge=None, monthlyDiscount=None, name="", shortName=""):
        self.action = action
        self.category = category
        self.characteristics = characteristics if characteristics else []
        self.classification = classification
        self.code = code
        self.customerRelevant = customerRelevant
        self.flexibleSwitch = flexibleSwitch if flexibleSwitch else FlexibleSwitch()
        self.insurance = insurance if insurance else Insurance()
        self.insuranceClass = insuranceClass
        self.isSecretNumber = isSecretNumber
        self.monthlyCharge = monthlyCharge if monthlyCharge else MonthlyCharge()
        self.monthlyDiscount = monthlyDiscount if monthlyDiscount else MonthlyDiscount()
        self.name = name
        self.shortName = shortName