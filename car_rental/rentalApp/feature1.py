import re


def get_rental_location() -> tuple | bool:
    try:
        street: str = input("[1/20] Podaj ulicę odbioru: ")
        if not re.match(r"^[0-9a-zA-ZąćęłńóśżźĄĆĘŁŃÓŚŻŹ\s-]+$", street):
            raise ValueError("Nieprawidłowa nazwa ulicy. Spróbuj ponownie.")

        postal_code: str = input("[2/20] Podaj kod pocztowy odbioru (format: XX-XXX): ")
        if not re.match(r"^\d{2}-\d{3}$", postal_code):
            raise ValueError("Nieprawidłowy kod pocztowy. Spróbuj ponownie.")

        city: str = input("[3/20] Podaj nazwę miasta: ")
        if not re.match(r"^[0-9a-zA-ZąćęłńóśżźĄĆĘŁŃÓŚŻŹ\s-]+$", city):
            raise ValueError("Nieprawidłowa nazwa miasta. Spróbuj ponownie.")

        # Formatowanie argumentów
        street = street.title()
        city = city.title()

        # Zwracanie argumentów
        return street, postal_code, city

    except ValueError as ve:
        print(ve)
        return False
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return False


def main():
    print(get_rental_location())


if __name__ == "__main__":
    main()
