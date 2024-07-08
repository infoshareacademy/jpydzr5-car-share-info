from feature1 import get_rental_location
from feature2 import get_rental_period
from feature3 import choose_car_category
from feature4 import choose_extras
from feature5 import get_personal_data
from feature6 import get_user_address
from feature7 import show_offer
from select_user_8 import select_user
from admin_edit_preorder_9 import select_preorder
from json_handler import json_user_data_reader, json_user_data_writer
from database_handler import connect_to_database, close_database_connection, create_preorder, update_preorder, confirm_preorder

def rental_app() -> None | Exception:
    conn = connect_to_database()
    try:
        # Create preorder at the beginning of the process
        preorder_id = create_preorder(conn)
        print(preorder_id)

        # Unpacking values from select_user
        user_id = select_user()
        update_preorder(conn, preorder_id, 'order_user_id', user_id[0])

        # Unpacking values from feature1
        street, postal_code, city = get_rental_location()  # type: ignore
        update_preorder(conn, preorder_id, 'order_street', street)
        update_preorder(conn, preorder_id, 'order_postal_code', postal_code)
        update_preorder(conn, preorder_id, 'order_city', city)

        # Unpacking values from feature2
        start_date, start_time, end_date, end_time = get_rental_period() # type: ignore
        update_preorder(conn, preorder_id, 'order_start_date', start_date)
        update_preorder(conn, preorder_id, 'order_start_time', start_time)
        update_preorder(conn, preorder_id, 'order_end_date', end_date)
        update_preorder(conn, preorder_id, 'order_end_time', end_time)

        # Unpacking values from feature3
        car_category = choose_car_category()
        if car_category is False:
            raise Exception("Invalid car category")
        update_preorder(conn, preorder_id, 'order_car_category', car_category)

        # Unpacking values from feature4
        extras = choose_extras()
        if extras is False:
            raise Exception("Invalid extras")
        update_preorder(conn, preorder_id, 'order_extras', extras)

        # Unpacking values from feature5
        first_name, last_name, email, phone, pesel, license_number = get_personal_data()  # type: ignore
        update_preorder(conn, preorder_id, 'user_first_name', first_name)
        update_preorder(conn, preorder_id, 'user_last_name', last_name)
        update_preorder(conn, preorder_id, 'user_email', email)
        update_preorder(conn, preorder_id, 'user_phone', phone)
        update_preorder(conn, preorder_id, 'user_pesel', pesel)
        update_preorder(conn, preorder_id, 'user_license_number', license_number)

        # Unpacking values from feature6
        street_, apartment_number_, postal_code_, city_, country_ = get_user_address()  # type: ignore
        update_preorder(conn, preorder_id, 'user_street', street_)
        update_preorder(conn, preorder_id, 'user_apartment_number', apartment_number_)
        update_preorder(conn, preorder_id, 'user_postal_code', postal_code_)
        update_preorder(conn, preorder_id, 'user_city', city_)
        update_preorder(conn, preorder_id, 'user_country', country_)

        # Confirm the order
        confirm_preorder(conn, preorder_id)

        # Show confirm order details
        # details_confirm_preorder(conn, preorder_id)

        # Prepare functions to save to JSON
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
            "extras": extras,
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
    finally:
        close_database_connection(conn)

def main():
    try:
        mode = input(
            "Wybierz tryb procesu:\nUSER: Użytkownik\nADMIN: Administrator\n\nWpisz USER lub ADMIN: ").strip().upper()

        if mode == "ADMIN":
            context_admin_menu: int = int(
                input(
                    "\nWybierz opcję:\n"
                    "1. Edytuj zamówienie\n"
                    "\n* Wybierz opcję (): "
                )
            )
            if context_admin_menu == 1:
                print("Wybrano: Edytuj zamówienie")
                select_preorder()
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
                return False

        elif mode == "USER":
            context_rent_menu: int = int(
                input(
                    "Witaj w naszej wypożyczalni samochodów!\n"
                    "\n[1/3] Sprawdź ofertę\n"
                    "[2/3] Dokonaj rezerwacji\n"
                    "[3/3] Przejrzyj szczegóły rezerwacji\n"
                    "\n* Wybierz opcję (1/2/3): "
                )
            )
            if context_rent_menu in [1, 2, 3]:
                if context_rent_menu == 1:
                    show_offer()
                if context_rent_menu == 2:
                    rental_app()
                if context_rent_menu == 3:
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
# BUG: Changes names (features). [*]