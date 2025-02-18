from typing import Optional

from src.model.monthly_charge import MonthlyCharge
from src.model.monthly_discount import MonthlyDiscount


class ProductDetails:
    def __init__(self, name, current=None, disclaimers=None,
                 monthlyCharge: Optional[MonthlyCharge] =None,
                 monthlyDiscount: Optional[MonthlyDiscount] =None,
                 offeringDescriptionLong="",
                 offeringDescriptionShort="", shortName=""):
        self.name = name
        self.current = current
        self.disclaimers = disclaimers if disclaimers else []
        self.monthlyCharge = monthlyCharge
        self.monthlyDiscount = monthlyDiscount
        self.offeringDescriptionLong = offeringDescriptionLong
        self.offeringDescriptionShort = offeringDescriptionShort
        self.shortName = shortName