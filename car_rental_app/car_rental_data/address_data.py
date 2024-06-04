import re


class AddressData:
    def __init__(self, street, apartment_number, postal_code, city, country):
        self.street = street
        self.apartment_number = apartment_number
        self.postal_code = postal_code
        self.city = city
        self.country = country

    @staticmethod
    def validate_postal_code(postal_code):
        return re.match(r"^\d{2}-\d{3}$", postal_code)

    def __str__(self):
        return f"{self.street} {self.apartment_number}, {self.postal_code} {self.city}, {self.country}"
