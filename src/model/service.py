from typing import Optional, List

from src.model.characteristic import Characteristic
from src.model.monthly_charge import MonthlyCharge


class Service:
    def __init__(
        self,
        action="",
        category="",
        characteristics: Optional[List['Characteristic']] = None,
        classification="",
        code="",
        customerRelevant=False,
        flexibleSwitch=None,
        insurance=None,
        insuranceClass="",
        isSecretNumber=False,
        monthlyCharge: Optional[MonthlyCharge] = None,
        monthlyDiscount=None,
        name="",
        shortName="",
        lifetimeInMonths=0,
        emailAddress=""
    ):
        self.action = action
        self.category = category
        self.characteristics = characteristics if characteristics is not None else []
        self.classification = classification
        self.code = code
        self.customerRelevant = customerRelevant
        self.flexibleSwitch = flexibleSwitch
        self.insurance = insurance
        self.insuranceClass = insuranceClass
        self.isSecretNumber = isSecretNumber
        self.monthlyCharge = monthlyCharge
        self.monthlyDiscount = monthlyDiscount
        self.name = name
        self.shortName = shortName
        self.lifetimeInMonths = lifetimeInMonths
        self.emailAddress = emailAddress
