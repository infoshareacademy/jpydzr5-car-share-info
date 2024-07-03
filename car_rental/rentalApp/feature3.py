from database_handler import connect_to_database, close_database_connection

def fetch_cars_data(conn):
    try:
        cursor = conn.cursor()
        query = """
            SELECT 
                cc.cat_id AS cat_id,
                cc.description AS category,
                cc.price AS price, 
                c.brand AS brand,
                c.model AS model
            FROM cars c
            LEFT JOIN car_categories cc ON cc.cat_id = c.car_category
        """
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return []

def choose_car_category() -> int | bool:
    try:
        # Connect to the database
        conn = connect_to_database()
        if not conn:
            return False

        # Fetch data from the database
        rows = fetch_cars_data(conn)
        if not rows:
            return False

        # Initialize categories dictionary
        categories = {}

        # Process query results
        for row in rows:
            cat_id = row[0]
            category = row[1]
            price = row[2]
            brand_model = f"{row[3]} {row[4]}"

            categories[category.lower()] = {"cat_id": cat_id, "price": price, "examples": []}

        # Close the database connection
        close_database_connection(conn)

        # Print available categories
        print("[8/20] Dostępne kategorie aut:")

        for category, car_info in categories.items():
            price = car_info["price"]
            examples = car_info["examples"]

            # Print category header
            print(f"\n{category.capitalize()}:")

            # Print price information
            print(f"\tW cenie {price:.2f}$ za dzień")

            # Print car examples
            print("\tModele dostępne w kategorii:")
            for example in examples:
                print(f"\t\t- {example}")

        # Prompt user for input
        while True:
            car_category_name: str = input(
                "Wybierz kategorię auta (Compact, Economy, Medium, Mini, SUV)\nWpisz tutaj: "
            ).strip().lower()  # Normalizacja wejścia użytkownika

            if car_category_name in categories:
                car_category_id = categories[car_category_name]["cat_id"]
                print(f"Wybrano kategorię: {car_category_name.capitalize()}")
                return car_category_id

            print(f"Nieprawidłowa kategoria. Spróbuj ponownie.")

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    choose_car_category()

if __name__ == "__main__":
    main()
