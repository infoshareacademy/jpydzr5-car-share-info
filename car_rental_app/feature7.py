def show_offer():
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

    print("Nasza oferta samochodów podzielonych na kategorie.")
    for category, car_info in categories.items():
        price = car_info["price"]
        examples = car_info["examples"]

        # Print category header
        print(f"\n* Kategoria {category}:")

        # Print price information
        print(f"\n\tW cenie {price:.2f}$")

        # Print car examples
        print("\tPrzykłady samochodów:")
        for example in examples:
            print(f"\t\t- {example}")


def main():
    show_offer()


if __name__ == "__main__":
    main()
