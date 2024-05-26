class CarCategory:
    categories = {
        "A": {"price": 100.00, "examples": ["Toyota Aygo", "Fiat 500", "VW Up", "Kia Picanto"]},
        "B": {"price": 200.00, "examples": ["VW Golf", "Ford Focus", "Opel Astra", "Toyota Corolla"]}
    }

    def __init__(self, category, rental_days):
        self.category = category
        self.price_per_day = self.categories[category]["price"]
        self.examples = self.categories[category]["examples"]
        self.total_cost = self.price_per_day * rental_days

    def __str__(self):
        return f"Kategoria {self.category}, Koszt: {self.total_cost:.2f} PLN, Przykłady: {', '.join(self.examples)}"

