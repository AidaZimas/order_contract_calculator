
from product import Product


class Subscription:
    def __init__(self, product, services, switch=None):
        self.product = product
        self.services = services
        self.switch = switch

    def get_product(self):
        return self.product

    def get_services(self):
        return self.services

    def get_switch(self):
        return self.switch

    def has_attribute_value(self, attribute):
        return hasattr(self, attribute)

    def get_attribute_value(self, attribute):
        value = getattr(self, attribute, None)
        
        if isinstance(value, Product):
            return value.name  
        
        parts = attribute.split(".") 
        
        return value

    def __repr__(self):
        return f"Subscription(product={self.product}, services={self.services}, switch={self.switch})"