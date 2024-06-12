import re


def get_rental_location() -> tuple:
    try:
        street: str = input("[1/12] Podaj ulicę odbioru: ")
        if not re.match(r"^\D+$", street):
            raise ValueError("Nieprawidłowa nazwa ulicy. Spróbuj ponownie.")

        postal_code: str = input("[2/12] Podaj kod pocztowy odbioru(format: XX-XXX): ")
        if not re.match(r"^\d{2}-\d{3}$", postal_code):
            raise ValueError("Nieprawidłowy kod pocztowy. Spróbuj ponownie.")

        city: str = input("[3/12] Podaj nazwę miasta: ")
        if not re.match(r"^\D+$", city):
            raise ValueError("Nieprawidłowa nazwa miasta. Spróbuj ponownie.")

        return street, postal_code, city
    except Exception as e:
        print(e)


def main():
    print(get_rental_location())


if __name__ == "__main__":
    main()
