from json_handler import json_reader

# Read from the JSON file
instance_001 = json_reader(path="static/json/id_001.json")

# Print values from the instance
print(f"Brand: {instance_001['id_001']['brand']}")
print(f"Model: {instance_001['id_001']['model']}")

##

import datetime
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


class RentalPeriod:
    def __init__(self, start_date, start_time, end_date, end_time):
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time

    @staticmethod
    def validate_date(date_str):
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if date < datetime.date.today():
                return False
            return date
        except ValueError:
            return False

    @staticmethod
    def validate_time(time_str):
        try:
            time = datetime.datetime.strptime(time_str, "%H:%M").time()
            if datetime.time(6, 0) <= time <= datetime.time(23, 0):
                return time
            return False
        except ValueError:
            return False

    def rental_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self):
        return f"Odbiór: {self.start_date} {self.start_time}, Zwrot: {self.end_date} {self.end_time}"


class CarCategory:
    categories = {
        "A": {"price": 100.00, "examples": ["Toyota Aygo", "Fiat 500", "VW Up", "Kia Picanto"]},
        "B": {"price": 200.00, "examples": ["VW Golf", "Ford Focus", "Opel Astra", "Toyota Corolla"]}
    }

    def __init__(self, category, rental_days):
        self.category = category
        self.price_per_day = self.categories[category]["price"]
        self.examples = self.categories[category]["examples"]
        self.total_cost = self.price_per_day * rental_days

    def __str__(self):
        return f"Kategoria {self.category}, Koszt: {self.total_cost:.2f} PLN, Przykłady: {', '.join(self.examples)}"


class Extras:
    extras_costs = {
        "extended_insurance": 30.00,
        "abroad_travel": 40.00
    }

    def __init__(self, rental_days):
        self.rental_days = rental_days
        self.selected_extras = {}

    def add_extra(self, extra_name):
        if extra_name in self.extras_costs:
            self.selected_extras[extra_name] = self.extras_costs[extra_name] * self.rental_days

    def total_cost(self):
        return sum(self.selected_extras.values())

    def __str__(self):
        extras_str = ", ".join([f"{extra}: {cost:.2f} PLN" for extra, cost in self.selected_extras.items()])
        return extras_str


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


class CarRental:
    def __init__(self):
        self.rental_start = None
        self.rental_end = None
        self.car_category = None
        self.extras = None
        self.personal_data = None
        self.address_data = None

    def get_rental_location(self, prompt):
        while True:
            street = input(f"Podaj ulicę {prompt}: ")
            postal_code = input(f"Podaj kod pocztowy {prompt} (format: XX-XXX): ")
            if RentalLocation.validate_postal_code(postal_code):
                return RentalLocation(street, postal_code)
            else:
                print("Nieprawidłowy kod pocztowy. Spróbuj ponownie.")

    def get_rental_period(self):
        while True:
            start_date = input("Podaj datę rozpoczęcia wynajmu (YYYY-MM-DD): ")
            start_date = RentalPeriod.validate_date(start_date)
            if not start_date:
                print("Nieprawidłowy format daty lub data przeszła. Spróbuj ponownie.")
                continue

            start_time = input("Podaj godzinę odbioru (format HH:MM, między 06:00 a 23:00): ")
            start_time = RentalPeriod.validate_time(start_time)
            if not start_time:
                print("Nieprawidłowy format godziny lub godzina poza zakresem. Spróbuj ponownie.")
                continue

            end_date = input("Podaj datę zakończenia wynajmu (YYYY-MM-DD): ")
            end_date = RentalPeriod.validate_date(end_date)
            if not end_date:
                print("Nieprawidłowy format daty lub data przeszła. Spróbuj ponownie.")
                continue

            end_time = input("Podaj godzinę zwrotu (format HH:MM, między 06:00 a 23:00): ")
            end_time = RentalPeriod.validate_time(end_time)
            if not end_time:
                print("Nieprawidłowy format godziny lub godzina poza zakresem. Spróbuj ponownie.")
                continue

            if end_date < start_date or (end_date == start_date and end_time <= start_time):
                print("Data zwrotu nie może być wcześniejsza niż data odbioru. Spróbuj ponownie.")
                continue

            return RentalPeriod(start_date, start_time, end_date, end_time)

    def choose_car_category(self, rental_days):
        while True:
            print("\nDostępne kategorie aut:")
            for category, details in CarCategory.categories.items():
                print(
                    f"Kategoria {category}: {details['price']} PLN za dzień, Przykłady: {', '.join(details['examples'])}")

            car_category = input("Wybierz kategorię auta (A/B): ").upper()
            if car_category in CarCategory.categories:
                return CarCategory(car_category, rental_days)
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

    def choose_extras(self, rental_days):
        extras = Extras(rental_days)
        while True:
            print("\nDostępne dodatki:")
            print("1. Rozszerzona polisa ubezpieczeniowa: 30.00 PLN za dzień")
            print("2. Wyjazd za granicę: 40.00 PLN za dzień")
            print("3. Brak dodatków")

            extra_choice = input("Wybierz dodatki (1/2/3): ")

            if extra_choice == "1":
                extras.add_extra("extended_insurance")
            elif extra_choice == "2":
                extras.add_extra("abroad_travel")
            elif extra_choice == "3":
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
                continue

            break

        return extras

    def get_personal_data(self):
        while True:
            first_name = input("Podaj imię: ")
            last_name = input("Podaj nazwisko: ")
            email = input("Podaj email: ")
            if not PersonalData.validate_email(email):
                print("Nieprawidłowy email. Spróbuj ponownie.")
                continue
            phone = input("Podaj numer kontaktowy: ")
            if not PersonalData.validate_phone(phone):
                print("Nieprawidłowy numer kontaktowy. Spróbuj ponownie.")
                continue
            pesel = input("Podaj PESEL: ")
            if not PersonalData.validate_pesel(pesel):
                print("Nieprawidłowy PESEL. Spróbuj ponownie.")
                continue
            license_number = input("Podaj nr prawa jazdy: ")
            if not PersonalData.validate_license_number(license_number):
                print("Nieprawidłowy nr prawa jazdy. Spróbuj ponownie.")
                continue
            break

        return PersonalData(first_name, last_name, email, phone, pesel, license_number)

    def get_address_data(self):
        while True:
            street = input("Podaj ulicę: ")
            apartment_number = input("Podaj numer lokalu: ")
            postal_code = input("Podaj kod pocztowy (format: XX-XXX): ")
            if not AddressData.validate_postal_code(postal_code):
                print("Nieprawidłowy kod pocztowy. Spróbuj ponownie.")
                continue
            city = input("Podaj miasto: ")
            country = input("Podaj kraj (np. Polska): ")
            break

        return AddressData(street, apartment_number, postal_code, city, country)

    def summary(self):
        rental_days = self.rental_period.rental_days()
        total_rental_cost = self.car_category.total_cost
        total_extras_cost = self.extras.total_cost()
        total_cost = total_rental_cost + total_extras_cost

        print("\nPodsumowanie rezerwacji:")
        print(f"\nDane osobowe: {self.personal_data}")
        print(f"\nDane adresowe: {self.address_data}")
        print("\nRezerwacja:")
        print(f"Miejsce odbioru: {self.rental_start}")
        print(f"Data i godzina odbioru: {self.rental_period.start_date} {self.rental_period.start_time}")
        print(f"Miejsce zwrotu: {self.rental_end}")
        print(f"Data i godzina zwrotu: {self.rental_period.end_date} {self.rental_period.end_time}")
        print(f"Liczba dni najmu: {rental_days}")
        print(f"Kategoria auta: {self.car_category}, Koszt: {total_rental_cost:.2f} PLN")
        print("Dodatki:", self.extras)
        print(f"Koszt całkowity wynajmu: {total_cost:.2f} PLN")

        while True:
            action = input("\nWybierz opcję:\n1. Rezerwuję\n2. Edytuj dane\nTwój wybór: ")
            if action == "1":
                print("Rezerwacja została dokonana.")
                break
            elif action == "2":
                return False
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
        return True

    def run(self):
        while True:
            self.rental_start = self.get_rental_location("odbioru")
            self.rental_end = self.get_rental_location("zwrotu")
            self.rental_period = self.get_rental_period()
            self.car_category = self.choose_car_category(self.rental_period.rental_days())
            self.extras = self.choose_extras(self.rental_period.rental_days())
            self.personal_data = self.get_personal_data()
            self.address_data = self.get_address_data()

            if self.summary():
                break


if __name__ == "__main__":
    CarRental().run()
