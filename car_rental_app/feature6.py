import re


def get_user_address() -> tuple | bool:
    try:
        print("Poniżej uzupełnij swoje dane adresowe.")
        street: str = input("[16/20] Podaj ulicę: ")
        if not re.match(r"^\D+$", street):
            raise ValueError("Nieprawidłowa nazwa ulicy. Spróbuj ponownie.")

        apartment_number: str = input("[17/20] Podaj numer lokalu: ")
        # missing regex

        postal_code: str = input("[18/20] Podaj kod pocztowy (format: XX-XXX): ")
        if not re.match(r"^\d{2}-\d{3}$", postal_code):
            raise ValueError("Nieprawidłowy kod pocztowy. Spróbuj ponownie.")

        city: str = input("[19/20] Podaj nazwę miasta: ")
        if not re.match(r"^\D+$", city):
            raise ValueError("Nieprawidłowa nazwa miasta. Spróbuj ponownie.")

        country: str = input("[20/20] Podaj kraj: ")
        if not re.match(r"^\D+$", country):
            raise ValueError("Nieprawidłowy kraj. Spróbuj ponownie.")

        # format arguments
        street = street.title()
        apartment_number = apartment_number.title()
        postal_code = postal_code
        city = city.title()
        country = country.title()

        # return arguments
        return street, apartment_number, postal_code, city, country

    except Exception as e:
        print(e)
        return False


def main():
    print(get_user_address())


if __name__ == "__main__":
    main()
