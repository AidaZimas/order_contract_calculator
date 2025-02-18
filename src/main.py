import json
import math

from initializer import initialize_subscription
from src.row_offering import RowForOffering
from src.utils.contract_helpers import find_telia_finance_switch, find_characteristic_value, find_extra_insurance

with open("../3917109.json", 'r') as cache_file:
    product_data = json.load(cache_file)

subscription = initialize_subscription(product_data)

# SWITCH
is_switch_enabled = False
rows_for_switch = []
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

    rows_for_switch.append(RowForOffering(f"Telefon: {switch_phone_model}", switch_base_price, "false"))

    if switch_imei is not None:
        rows_for_switch.append(RowForOffering(f"IMEI: {switch_imei}", "", "false"))

    rows_for_switch.append(RowForOffering(
        f"SVITSJ Skjermforsikring: {switch_included_insurance_ex_vat} kr mva-fritt {switch_months} md",
        switch_included_insurance_ex_vat,
        "false"
    ))

    price_per_month = int(math.ceil(switch_included_insurance_ex_vat))
    total_price = switch_total

product_price = 0
discount_duration = 0
rows_for_offering = []
# Abonnement
if subscription.product is not None:
    product = subscription.product
    product_price = float(product.monthlyCharge.inVat)
    product_discount = product.monthlyDiscount.inVat
    discount_duration = product.monthlyDiscount.durationInMonths

    product_price = product_price - product_discount

    rows_for_offering.append(RowForOffering(
        subscription.product.name,
        product_price,
        "false"
    ))

    if product_discount > 0.00:
        offering_discount_text = f"{discount_duration} måneder" if discount_duration > 0 else "kampanjeperiode"

        rows_for_offering.append(RowForOffering(
            offering_discount_text,
            product_price,
            "false"
        ))

total_discount = 0
total_service_price = 0
rows_for_services_deleted = []
rows_for_services_added = []
# Tjenester
for service in subscription.services:
    service_name = service.name
    service_price = float(service.monthlyCharge.inVat)

    if (service.action == 'ADD' and service.customerRelevant != False
            and service.flexibleSwitch.isTeliaFinance is not True
            and not (service.insuranceClass == "SWITCH" and switch_associated_service is not None)
            and service.category not in ['LEAS_FLEX', 'LEASE12', 'LEASE24']):

        lifetime = int(service.lifetimeInMonths)

        if service_price < 0:  # discounts
            total_discount += service_price
            rows_for_services_added.append(RowForOffering(
                service_name,
                service_price,
                False
            ))
        else:
            total_service_price += service_price
            rows_for_services_added.append(RowForOffering(
                service_name,
                service_price,
                False
            ))

    elif service.action == 'DELETE' and service.customerRelevant:
        rows_for_services_deleted.append(RowForOffering(
            service_name,
            service_price,
            False
        ))

commitment_duration = 12
total_discount = math.ceil(abs(total_discount))
discounted_price = (product_price + total_service_price) - total_discount
total_discounted_price = discounted_price * discount_duration
total_not_discounted_price = (product_price + total_service_price) * (commitment_duration - discount_duration)
price_per_month = math.ceil(discounted_price)
total_price = math.ceil(total_discounted_price + total_not_discounted_price)
price_per_month_caption = ""
if discount_duration > 0:
    if discount_duration == 1:
        price_per_month_caption = "Betaler for en måned med rabatt"
    else:
        price_per_month_caption = f"Å betale per måned, de første {discount_duration} månedene"


if is_switch_enabled:
    print(RowForOffering("", "", "false").toTableRow())
    print(RowForOffering("---Svitsj", "", "false").toTableRow())
    for row in rows_for_switch:
         print(row.toTableRow())

if len(rows_for_offering) > 0:
    print(RowForOffering("", "", "false").toTableRow())
    print(RowForOffering("---Abonnement", "", "false").toTableRow())
    for row in rows_for_offering:
         print(row.toTableRow())

if len(rows_for_services_added) > 0:
    print(RowForOffering("", "", "false").toTableRow())
    print(RowForOffering("---Tjenester", "", "false").toTableRow())
    for row in rows_for_services_added:
         print(row.toTableRow())

if len(rows_for_services_deleted) > 0:
    print(RowForOffering("", "", "false").toTableRow())
    print(RowForOffering("Deleted", "", "false").toTableRow())
    for row in rows_for_services_deleted:
        print(row.toTableRow())

print(f"\nMinste totalpris {total_price}")
print(f"{price_per_month_caption} {price_per_month}")
