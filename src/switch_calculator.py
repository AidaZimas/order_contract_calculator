from collections import defaultdict
import json
from database import OracleDatabase
from product import Product
from model.service import Service
from model.subscription import Subscription
from switch import Switch

# Database connection details
dsn = "your_dsn"
user = "your_user"
password = "your_password"

db = OracleDatabase(dsn, user, password)
db.connect()

order_id = 3917109
product_data = db.fetch_data(order_id)
db.close()

product_data_dict = {item["NAME"]: item["TEXT_VALUE"] for item in product_data}

# Wrap into Subscription class
product = Product(
    name=product_data_dict.get("subscriptions[1].product"),
    monthly_charge_in_vat=product_data_dict.get("subscriptions[1].product.current.monthlyCharge.inVat"),
    monthly_discount_in_vat=product_data_dict.get("subscriptions[1].product.monthlyDiscount.inVat"),
    discount_duration_in_months=product_data_dict.get("subscriptions[1].product.monthlyDiscount.durationInMonths"),
)

services_dict = defaultdict(dict)
for item in product_data:
    key, value = item["NAME"], item["TEXT_VALUE"]
    if "subscriptions[1].services[" in key:
        service_index = int(key.split("services[")[1].split("]")[0])
        attribute_name = key.split(f"services[{service_index}].")[1]
        services_dict[service_index][attribute_name] = value

services = [
    Service(
        name=service_data.get("name"),
        monthly_charge_in_vat=service_data.get("monthlyCharge.inVat"),
        action=service_data.get("action"),
        customer_relevant=service_data.get("customerRelevant") == "true",
        flexible_switch_is_telia_finance=False,
        insurance_class=None,
        category=service_data.get("category"),
        lifetime_in_months=service_data.get("lifetimeInMonths"),
    )
    for service_data in services_dict.values()
]

switch_dict = {
    key.split("subscriptions[1].switch.")[1]: value
    for key, value in product_data_dict.items()
    if "subscriptions[1].switch." in key
}

switch = Switch(
    number_of_installments=switch_dict.get("numberOfInstallments"),
    installment_amount_in_vat=switch_dict.get("installmentAmount.inVat"),
    included_insurance_in_vat=switch_dict.get("includedInsurance.inVat"),
    included_insurance_ex_vat=switch_dict.get("includedInsurance.exVat"),
    model=switch_dict.get("model"),
    imei=switch_dict.get("imei"),
) if switch_dict else None

subscription = Subscription(product, services, switch)

print(subscription.get_attribute_value("product"))
print(subscription.get_attribute_value("product.monthlyCharge.inVat"))
print(subscription.get_attribute_value("product.monthlyDiscount.inVat"))
print(subscription.get_attribute_value("product.monthlyDiscount.durationInMonths"))
print(subscription.get_attribute_value("services"))