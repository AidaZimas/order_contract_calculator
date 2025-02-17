import json
import math

from initializer import initialize_subscription
from src.model.product_details import ProductDetails
from src.row_offering import RowForOffering
from src.utils.contract_helpers import find_telia_finance_switch, find_characteristic_value, find_extra_insurance

with open("../3917109.json", 'r') as cache_file:
    product_data = json.load(cache_file)

subscription = initialize_subscription(product_data)
is_switch_enabled = False
rows_to_print = []

# SWITCH
switch_associated_service = find_telia_finance_switch(subscription.services, 'ADD')

if subscription.downPayment.numberOfInstallments > 0 and switch_associated_service is not None:
    is_switch_enabled = True
    switch_months = switch_associated_service.flexibleSwitch.numberOfInstallments
    switch_full_price = switch_associated_service.flexibleSwitch.installmentAmountInVat

    switch_included_insurance_in_vat = switch_associated_service.flexibleSwitch.includedInsuranceInVat
    switch_included_insurance_ex_vat = switch_associated_service.flexibleSwitch.includedInsuranceExVat

    switch_base_price = switch_full_price - switch_included_insurance_in_vat
    switch_phone_model = find_characteristic_value(switch_associated_service, 'MODEL')
    switch_imei = find_characteristic_value(switch_associated_service, 'IMEI')
    switch_monthly_total = switch_full_price
    switch_total = switch_full_price * switch_months

    extra_insurance = find_extra_insurance(subscription.services, "ADD", "SWITCH")
    # print(extra_insurance)

    rows_to_print.append(RowForOffering("Svitsj", "", "false"))
    rows_to_print.append(RowForOffering(f"Telefon: {switch_phone_model}", switch_base_price, "false"))

    if switch_imei is not None:
        rows_to_print.append(RowForOffering(f"IMEI: {switch_imei}", "", "false"))

    rows_to_print.append(RowForOffering(
        f"SVITSJ Skjermforsikring: {switch_included_insurance_ex_vat} kr mva-fritt {switch_months} md",
        switch_included_insurance_ex_vat,
        "false"
    ))

    pricePerMonth = int(math.ceil(switch_included_insurance_ex_vat))
    totalPrice = switch_total


rows_to_print.append(RowForOffering("Abonnement", "", "false"))

if subscription.product is not None:
    product = subscription.product
    product_price = float(product.monthlyCharge.inVat)
    product_discount = 0
    discount_duration = 0
    product_price -= product_discount

    rows_to_print.append(RowForOffering(
        subscription.product,
        product_price,
        "false"
    ))


    if product_discount > 0.00:
        offering_discount_text = "kampanjeperiode"
        rows_to_print.append(RowForOffering(
            offering_discount_text,
            product_price,
            "false"
        ))


for row in rows_to_print:
    print(row.toTableRow())