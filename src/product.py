class Product:
    def __init__(self, name, monthly_charge_in_vat, monthly_discount_in_vat, discount_duration_in_months):
        self.name = name
        self.monthly_charge_in_vat = monthly_charge_in_vat
        self.monthly_discount_in_vat = monthly_discount_in_vat
        self.discount_duration_in_months = discount_duration_in_months

    def has_attribute_value(self, attribute):
        return hasattr(self, attribute)

    def get_attribute_value(self, attribute):
        return getattr(self, attribute, None)

    def __repr__(self):
        return (f"Product(name='{self.name}', monthly_charge_in_vat={self.monthly_charge_in_vat}, "
                f"monthly_discount_in_vat={self.monthly_discount_in_vat}, discount_duration_in_months={self.discount_duration_in_months})")