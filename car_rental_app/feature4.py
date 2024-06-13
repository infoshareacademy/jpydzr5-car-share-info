def choose_extras() -> str | bool:
    one: str = "Rozszerzona polisa ubezpieczeniowa: 30.00 PLN za dzień"
    two: str = "Wyjazd za granicę: 40.00 PLN za dzień"
    three: str = "Brak dodatkowego ubezpieczenia"

    print("[9/12] Dostępne dodatki:")
    print(f"1. {one}")
    print(f"2. {two}")
    print(f"3. {three}")

    try:
        insurance: int = int(input("Wybierz dodatki (1/2/3): "))

        if insurance == 1:
            print(f"Wybrano: {one}")
            return one
        elif insurance == 2:
            print(f"Wybrano: {two}")
            return two
        elif insurance == 3:
            print(f"Wybrano: {three}")
            return three
        else:
            raise ValueError

    except ValueError:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        return False


def main():
    choose_extras()


if __name__ == "__main__":
    main()
