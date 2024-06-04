from car_rental_data.rental_location import RentalLocation
from car_rental_data.rental_period import RentalPeriod
from car_rental_data.car_category import CarCategory
from car_rental_data.extras import Extras
from car_rental_data.personal_data import PersonalData
from car_rental_data.address_data import AddressData


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
                    f"Kategoria {category}: {details['price']} PLN za dzień, "
                    f"Przykłady: {', '.join(details['examples'])}")

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
