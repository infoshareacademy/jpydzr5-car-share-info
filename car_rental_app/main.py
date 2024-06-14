from feature1 import get_rental_location
from feature2 import get_rental_period
from feature3 import choose_car_category
from feature4 import choose_extras
from feature5 import get_personal_data
from feature6 import get_user_address
from feature7 import show_offer
from json_handler import json_user_data_reader, json_user_data_writer


def rental_app() -> None | Exception:
    try:
        # Unpacking values from feature1
        street, postal_code, city = get_rental_location()  # type: ignore

        # Unpacking values from feature2
        start_date, start_time, end_date, end_time = get_rental_period()  # type: ignore

        # Unpacking values from feature3
        car_category = choose_car_category()
        if car_category is False:
            raise

        # Unpacking values from feature4
        insurance = choose_extras()
        if insurance is False:
            raise

        # Unpacking values from feature5
        first_name, last_name, email, phone, pesel, license_number = get_personal_data()  # type: ignore

        # Unpacking values from feature6
        street_, apartment_number_, postal_code_, city_, country_ = get_user_address()  # type: ignore

        # Prepare functions to save to json
        data = {
            # feature1
            "street": street,
            "postal_code": postal_code,
            "city": city,
            # feature2
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
            # feature3
            "car_category": car_category,
            # feature4
            "insurance": insurance,
            # feature5
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "pesel": pesel,
            "license_number": license_number,
            # feature6
            "street_": street_,
            "apartment_number_": apartment_number_,
            "postal_code_": postal_code_,
            "city_": city_,
            "country_": country_,
        }

        # JSON user_data_writer
        json_user_data_writer(path="json/user_data.json", function_data=data)

    except Exception as e:
        return e


def main():
    try:
        context_menu: int = int(
            input(
                "Witaj w naszej wypożyczalni samochodów!\n"
                "\n[1/3] Sprawdź ofertę\n"
                "[2/3] Dokonaj rezerwacji\n"
                "[3/3] Przejrzyj szczegóły rezerwacji\n"
                "\n* Wybierz opcję (1/2/3): "
            )
        )

        if context_menu in [1, 2, 3]:
            if context_menu == 1:
                show_offer()
            if context_menu == 2:
                rental_app()
            if context_menu == 3:
                context = [
                    "1. Ulica odbioru",
                    "2. Kod pocztowy",
                    "3. Miasto",
                    "4. Data rezerwacji",
                    "5. Godzina rozpoczęcia rezerwacji",
                    "6. Data zakończenia rezerwacji",
                    "7. Godzina zakończenia rezerwacji",
                    "8. Kategoria samochodu",
                    "9. Extra",
                    "10. Imię",
                    "11. Nazwisko",
                    "12. Email",
                    "13. Telefon",
                    "14. PESEL",
                    "15. Numer prawa jazdy",
                    "16. Ulica",
                    "17. Numer lokalu",
                    "18. Kod pocztowy",
                    "19. Miasto",
                    "20. Kraj",
                ]
                # JSON user_data_reader
                data = json_user_data_reader(path="json/user_data.json")
                counter = 0
                for key, value in data.items():
                    print(f"   * {context[counter]}: {value}")
                    counter += 1
        else:
            raise ValueError

    except ValueError:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()

# BUG: Missing logic with renting a car by user. [main, car_template]
# BUG: There's no minimal rental period. [feature2]
# BUG: End_date can be past start_date. [feature2]
# BUG: Categories from feature3 could be automated. Based on car_template. [feature3]
# BUG: Missing prices for rental. [feature3, feature4]
# BUG: Missing regex for apartment_number. [feature6]
# BUG: feature7 is a copy of feature3 without logic, it is not automated. [feature7]
# BUG: pytest is not working as expected. [pytest]
# BUG: Calculator for evaluating how much user would have to pay, including rental days, hours & mileage treshold. It should be available for user & superuser. It would be used implicitly to calc car rental cost. [app]
# BUG: UI for superuser with availability to browse list of all cars, their status, current rentals and availability to assign / change car for user before initial due date. [app]
# BUG: Forms for returning a car. [app]
# BUG: Mock payment status. If payment completed, confirmation should be generated for user with car details. [app]
