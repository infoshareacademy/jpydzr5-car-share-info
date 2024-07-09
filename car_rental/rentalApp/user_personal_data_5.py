import re


def get_personal_data() -> tuple | bool:
    try:
        first_name: str = input("[10/20] Podaj imię: ")
        if not re.match(r"^\D+$", first_name):
            raise ValueError("Nieprawidłowe imię. Spróbuj ponownie.")

        last_name: str = input("[11/20] Podaj nazwisko: ")
        if not re.match(r"^\D+$", last_name):
            raise ValueError("Nieprawidłowe nazwisko. Spróbuj ponownie.")

        email: str = input("[12/20] Podaj email: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Nieprawidłowy email. Spróbuj ponownie.")

        phone: str = input("[13/20] Podaj numer kontaktowy: ")
        if not re.match(r"^\d{9}$", phone):
            raise ValueError("Nieprawidłowy numer kontaktowy. Spróbuj ponownie.")

        pesel: str = input("[14/20] Podaj PESEL (np. 87021005862): ")
        if not re.match(r"^\d{11}$", pesel):
            raise ValueError("Nieprawidłowy PESEL. Spróbuj ponownie.")

        license_number: str = input("[15/20] Podaj nr prawa jazdy (np. XYZ98765): ")
        if not re.match(r"^[A-Z0-9]{5,}$", license_number):
            raise ValueError("Nieprawidłowy nr prawa jazdy. Spróbuj ponownie.")

        # format arguments
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
        email = email.lower()
        phone = phone
        pesel = pesel.upper()
        license_number = license_number.upper()

        # return arguments
        return first_name, last_name, email, phone, pesel, license_number

    except ValueError as e:
        print(e)
        return False


def main():
    get_personal_data()


if __name__ == "__main__":
    main()
