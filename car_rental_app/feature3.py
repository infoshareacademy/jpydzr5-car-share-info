def choose_car_category() -> str | bool:
    categories = {
        "Compact": {
            "price": 90.00,
            "examples": ["Toyota Corolla", "Volkswagen Golf", "Opel Astra"],
        },
        "Economy": {
            "price": 80.00,
            "examples": ["Toyota Yaris", "Volkswagen Polo", "Opel Corsa"],
        },
        "Medium": {
            "price": 100.00,
            "examples": ["BMW 3", "Audi A4", "Mercedes-Benz Class C"],
        },
        "Mini": {"price": 70.00, "examples": ["Toyota Aygo", "Fiat 500"]},
        "SUV": {"price": 120.00, "examples": ["Toyota RAV4", "BMW X3", "Audi Q3"]},
    }

    print("[8/20] Dostępne kategorie aut:")

    for category, car_info in categories.items():
        price = car_info["price"]
        examples = car_info["examples"]

        # Print category header
        print(f"\n{category}:")

        # Print price information
        print(f"\tW cenie {price:.2f}$")

        # Print car examples
        print("\tPrzykłady samochodów:")
        for example in examples:
            print(f"\t\t- {example}")

    try:
        car_category: str = input(
            "Wybierz kategorię auta (Compact, Economy, Medium, Mini, SUV)\nWpisz tutaj: "
        )

        car_category = car_category.lower()
        if car_category == "compact":
            car_category = "Compact"
        elif car_category == "economy":
            car_category = "Economy"
        elif car_category == "medium":
            car_category = "Medium"
        elif car_category == "mini":
            car_category = "Mini"
        elif car_category == "suv":
            car_category = "SUV"

        if car_category not in categories.keys():
            raise ValueError

        else:
            print(f"Wybrano kategorię: {car_category}")
            return car_category

    except ValueError:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        return False


def main():
    choose_car_category()


if __name__ == "__main__":
    main()
