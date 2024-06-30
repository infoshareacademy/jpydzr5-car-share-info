import os
import sqlite3

def connect_to_database(db_file):
    """ Establishes a connection to the SQLite database and returns the connection object """
    conn = sqlite3.connect(db_file)
    return conn

def close_database_connection(conn):
    """ Closes the connection to the SQLite database """
    conn.close()

def fetch_cars_data(conn):
    """ Executes an SQL query and returns the results """
    try:
        cursor = conn.cursor()

        # SQL query to fetch data from the cars and car_categories tables
        query = """SELECT 
                        cc.description AS category, 
                        cc.price AS price, 
                        c.brand AS brand,
                        c.model AS model
                    FROM cars c
                    LEFT JOIN car_categories cc ON cc.cat_id = c.car_category
                """
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows

    except sqlite3.Error as e:
        print(f"Wystąpił problem z bazą danych SQLite: {e}")
        return None

def show_offer(db_file):
    try:
        # Connect to the database
        conn = connect_to_database(db_file)

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

        # Zamknięcie połączenia z bazą danych
        close_database_connection(conn)

    except sqlite3.Error as e:
        print(f"Wystąpił problem z bazą danych SQLite: {e}")


def main():
    # os.path.dirname(__file__)
    #  - returns the directory where the current Python script is located.
    # os.path.dirname(os.path.dirname(__file__))
    #  - goes one level up to find the parent directory relative to the directory where the Python script is located.
    # os.path.join(..., 'car_rental')
    #  - combines the path to the db.sqlite3 file in the car_rental directory.

    db_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')

    # Call the function to display the car offer using the constructed database file path
    show_offer(db_file)


if __name__ == "__main__":
    main()