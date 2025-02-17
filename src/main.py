from collections import defaultdict
import json

from initializer import initialize_subscription
from switch import Switch

with open("3917109.json", 'r') as cache_file:
    product_data = json.load(cache_file)

# Initialize the Subscription class
subscription = initialize_subscription(product_data)

# Access attributes
print(subscription.billing.city)  # Output: Heimdal
print(subscription.product.current.name)  # Output: Telia Mobil 5 GB kr 329 med telefon og 12 mnd avtaletid
print(subscription.services[0].name)  # Output: Telia Finance SVITSJ i 24 md.