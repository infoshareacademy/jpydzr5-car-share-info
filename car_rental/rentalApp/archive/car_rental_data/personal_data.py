import re


class PersonalData:
    def __init__(self, first_name, last_name, email, phone, pesel, license_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.pesel = pesel
        self.license_number = license_number

    @staticmethod
    def validate_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def validate_phone(phone):
        return re.match(r"^\d{9}$", phone)

    @staticmethod
    def validate_pesel(pesel):
        return re.match(r"^\d{11}$", pesel)

    @staticmethod
    def validate_license_number(license_number):
        return re.match(r"^[A-Z0-9]{5,}$", license_number)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Email: {self.email}, Telefon: {self.phone}, PESEL: {self.pesel}, Prawo jazdy: {self.license_number}"
