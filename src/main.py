from collections import defaultdict
import json
import cx_Oracle
import os
import json
import cx_Oracle
from oracle_database import OracleDatabase
from product import Product
from service import Service
from subscription import Subscription
from switch import Switch

db = OracleDatabase()
db.connect()

order_id = 3917109  
cache_filename = f"{order_id}.json"

if os.path.exists(cache_filename):
    print(f"Using cached data from {cache_filename}")
    with open(cache_filename, 'r') as cache_file:
        product_data = json.load(cache_file)  
else:
    query = f"""
    SELECT a.NAME, a.TEXT_VALUE 
    FROM DOCUMENT d 
    INNER JOIN ATTRIBUTE a ON a.DOCUMENT_ID = d.DOCUMENT_ID 
    WHERE d.ORDER_ID = {order_id} 
    AND d.DOCUMENT_TYPE = 'PRIVATE_ORDER_CONTRACT' 
    ORDER BY NAME
    """

    results = db.execute_query(query)
    def lob_to_str(value):
        return value.read() if isinstance(value, cx_Oracle.LOB) else value

    product_data = [  
        {"NAME": lob_to_str(row[0]), "TEXT_VALUE": lob_to_str(row[1])}
        for row in results
    ]

    db.close()

    # Save fetched data in cache
    with open(cache_filename, 'w') as cache_file:
        json.dump(product_data, cache_file, indent=4)

    print(f"Data has been fetched and cached in {cache_filename}")


#print(product_data)

product_data_dict = {item["NAME"]: item["TEXT_VALUE"] for item in product_data}

# Wrap into Subscription class
product = Product(
    name=product_data_dict.get("subscriptions[1].product"),
    monthly_charge_in_vat=product_data_dict.get("subscriptions[1].product.current.monthlyCharge.inVat"),
    monthly_discount_in_vat=product_data_dict.get("subscriptions[1].product.monthlyDiscount.inVat"),
    discount_duration_in_months=product_data_dict.get("subscriptions[1].product.monthlyDiscount.durationInMonths"),
)

services_dict = defaultdict(dict)
services = []
for item in product_data:
    key, value = item["NAME"], item["TEXT_VALUE"]

    if "subscriptions[1].services[" in key:
        service_index = int(key.split("services[")[1].split("]")[0])  # Extract service index
        attribute_name = key.split(f"services[{service_index}].")[1]  # Extract attribute name
        services_dict[service_index][attribute_name] = value  # Store attribute

# Convert services_dict to a list of Service objects
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

# Extract switch-related attributes dynamically
switch_dict = {
    key.split("subscriptions[1].switch.")[1]: value
    for key, value in product_data_dict.items()
    if "subscriptions[1].switch." in key
}

# Create Switch object if relevant data exists
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
#print(subscription.get_attribute_value("product"))
#print(subscription.get_attribute_value("product"))