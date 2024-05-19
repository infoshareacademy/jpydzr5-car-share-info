import re

class RentalLocation:
    def __init__(self, street, postal_code):
        self.street = street
        self.postal_code = postal_code
        self.city = self.get_city_from_postal_code(postal_code)
        self.country = "Polska"

    @staticmethod
    def get_city_from_postal_code(postal_code):
        cities = {
            "00-001": "Warszawa",
            "31-001": "Kraków",
            "50-001": "Wrocław"
        }
        return cities.get(postal_code, "Nieznane miasto")

    @staticmethod
    def validate_postal_code(postal_code):
        return re.match(r"^\d{2}-\d{3}$", postal_code)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}, {self.country}"
