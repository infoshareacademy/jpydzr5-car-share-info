class Extras:
    extras_costs = {
        "extended_insurance": 30.00,
        "abroad_travel": 40.00
    }

    def __init__(self, rental_days):
        self.rental_days = rental_days
        self.selected_extras = {}

    def add_extra(self, extra_name):
        if extra_name in self.extras_costs:
            self.selected_extras[extra_name] = self.extras_costs[extra_name] * self.rental_days

    def total_cost(self):
        return sum(self.selected_extras.values())

    def __str__(self):
        extras_str = ", ".join([f"{extra}: {cost:.2f} PLN" for extra, cost in self.selected_extras.items()])
        return extras_str if extras_str else "Brak wybranych dodatków"
