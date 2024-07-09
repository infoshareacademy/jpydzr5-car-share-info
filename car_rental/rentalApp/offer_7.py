import sqlite3
from database_handler import connect_to_database, close_database_connection

def fetch_cars_data(conn):
    """Executes an SQL query and returns the results."""
    try:
        cursor = conn.cursor()
        query = """SELECT 
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
        print(f"Wystąpił problem z bazą danych SQLite: {e}")
        return None

def show_offer():
    try:
        # Connect to the database
        conn = connect_to_database()

        # Fetch data from the database
        rows = fetch_cars_data(conn)

        if rows:
            # Display the fetched data
            print("Nasza oferta samochodów podzielona na kategorie:")

            current_category = None
            for category, price, brand, model in rows:
                if category != current_category:
                    if current_category is not None:
                        print()  # New line between categories
                    print(f"* Kategoria {category}:")
                    current_category = category

                print(f"\n\tMarka: {brand}")
                print(f"\tModel: {model}")
                print(f"\tCena: {price:.2f}$")

        # Close the database connection
        close_database_connection(conn)
    except sqlite3.Error as e:
        print(f"Wystąpił problem z bazą danych SQLite: {e}")

def main():
    show_offer()

if __name__ == "__main__":
    main()
