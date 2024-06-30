import os
import sqlite3

def connect_to_database(db_file):
    """ Establishes a connection to the SQLite database and returns the connection object """
    conn = sqlite3.connect(db_file)
    return conn

def fetch_cars_data(conn):
    try:
        cursor = conn.cursor()
        query = """
            SELECT 
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
def choose_car_category(db_file) -> str | bool:
    try:
        # Connect to the database
        conn = connect_to_database(db_file)
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
            category = row[0]
            price = row[1]
            brand_model = f"{row[2]} {row[3]}"

            if category not in categories:
                categories[category] = {"price": price, "examples": []}

            categories[category]["examples"].append(brand_model)

        # Close the database connection
        conn.close()

        # Print available categories
        print("[8/20] Dostępne kategorie aut:")

        for category, car_info in categories.items():
            price = car_info["price"]
            examples = car_info["examples"]

            # Print category header
            print(f"\n{category}:")

            # Print price information
            print(f"\tW cenie {price:.2f}$ za dzień")

            # Print car examples
            print("\tModele dostępne w kategorii:")
            for example in examples:
                print(f"\t\t- {example}")

        # Prompt user for input
        car_category: str = input(
            "Wybierz kategorię auta (Compact, Economy, Medium, Mini, SUV)\nWpisz tutaj: "
        )

        # Normalize user input
        car_category = car_category.capitalize()

        if car_category not in categories.keys():
            raise ValueError("Nieprawidłowa kategoria.")

        print(f"Wybrano kategorię: {car_category}")
        return car_category

    except ValueError as ve:
        print(f"Nieprawidłowy wybór: {ve}. Spróbuj ponownie.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    # os.path.dirname(__file__)
    #  - returns the directory where the current Python script is located.
    # os.path.dirname(os.path.dirname(__file__))
    #  - goes one level up to find the parent directory relative to the directory where the Python script is located.
    # os.path.join(..., 'car_rental')
    #  - combines the path to the db.sqlite3 file in the car_rental directory.

    db_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')

    choose_car_category(db_file)


if __name__ == "__main__":
    main()
