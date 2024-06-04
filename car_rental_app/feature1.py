import re


def get_rental_location() -> tuple:
    try:

        street: str = input(f"[1/12] Podaj ulicę odbioru: ")
        # Add validation for the street

        postal_code: str = input(f"[2/12] Podaj kod pocztowy odbioru(format: XX-XXX): ")
        if not re.match(r"^\d{2}-\d{3}$", postal_code):
            raise ValueError("Nieprawidłowy kod pocztowy. Spróbuj ponownie.")

        city: str = input(f"[3/12] Podaj nazwę miasta: ")
        # Add validation for the city

        return street, postal_code, city

    except Exception as e:
        print(e)


def main():
    print(get_rental_location())


if __name__ == "__main__":
    main()
