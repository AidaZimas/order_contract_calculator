

class Switch:
    def __init__(self, number_of_installments, installment_amount_in_vat, included_insurance_in_vat, included_insurance_ex_vat, model, imei):
        self.number_of_installments = number_of_installments
        self.installment_amount_in_vat = installment_amount_in_vat
        self.included_insurance_in_vat = included_insurance_in_vat
        self.included_insurance_ex_vat = included_insurance_ex_vat
        self.model = model
        self.imei = imei

    def has_attribute_value(self, attribute):
        return hasattr(self, attribute)

    def get_attribute_value(self, attribute):
        return getattr(self, attribute, None)

    def __repr__(self):
        return (f"Switch(number_of_installments={self.number_of_installments}, installment_amount_in_vat={self.installment_amount_in_vat}, "
                f"included_insurance_in_vat={self.included_insurance_in_vat}, included_insurance_ex_vat={self.included_insurance_ex_vat}, "
                f"model='{self.model}', imei='{self.imei}')")