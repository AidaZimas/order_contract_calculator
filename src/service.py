
class Service:
    def __init__(self, name, monthly_charge_in_vat, action, customer_relevant, flexible_switch_is_telia_finance, insurance_class, category, lifetime_in_months=None):
        self.name = name
        self.monthly_charge_in_vat = monthly_charge_in_vat
        self.action = action
        self.customer_relevant = customer_relevant
        self.flexible_switch_is_telia_finance = flexible_switch_is_telia_finance
        self.insurance_class = insurance_class
        self.category = category
        self.lifetime_in_months = lifetime_in_months

    def has_attribute_value(self, attribute):
        return hasattr(self, attribute)

    def get_attribute_value(self, attribute):
        return getattr(self, attribute, None)

    def __repr__(self):
        return (f"Service(name='{self.name}', monthly_charge_in_vat={self.monthly_charge_in_vat}, action='{self.action}', "
                f"customer_relevant='{self.customer_relevant}', flexible_switch_is_telia_finance='{self.flexible_switch_is_telia_finance}', "
                f"insurance_class='{self.insurance_class}', category='{self.category}', lifetime_in_months={self.lifetime_in_months})")