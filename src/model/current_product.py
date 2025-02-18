class CurrentProduct:
    def __init__(self, name="", commitmentEnd="", commitmentStart="", disclaimers=None, hasActiveCommitment=False, monthlyCharge=None, offeringDescriptionLong="", offeringDescriptionShort="", shortName=""):
        self.name = name
        self.commitmentEnd = commitmentEnd
        self.commitmentStart = commitmentStart
        self.disclaimers = disclaimers if disclaimers else []
        self.hasActiveCommitment = hasActiveCommitment
        self.monthlyCharge = monthlyCharge
        self.offeringDescriptionLong = offeringDescriptionLong
        self.offeringDescriptionShort = offeringDescriptionShort
        self.shortName = shortName