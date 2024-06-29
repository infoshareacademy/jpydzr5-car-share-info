import os
import sqlite3

def connect_to_database(db_file):
    """ Funkcja łączy się z bazą danych SQLite i zwraca obiekt połączenia """
    conn = sqlite3.connect(db_file)
    return conn

def close_database_connection(conn):
    """ Funkcja zamyka połączenie z bazą danych """
    conn.close()

def fetch_cars_data(conn):
    """ Funkcja wykonuje zapytanie SQL i zwraca wyniki """
    try:
        cursor = conn.cursor()

        # Zapytanie SQL do pobrania danych z tabeli cars i car_categories
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
        # Połączenie z bazą danych
        conn = connect_to_database(db_file)

        # Pobranie danych z bazy danych
        rows = fetch_cars_data(conn)

        if rows:
            # Przetwarzanie wyników zapytania i wyświetlanie oferty
            print("Nasza oferta samochodów podzielona na kategorie:")

            current_category = None
            for category, price, brand, model in rows:
                if category != current_category:
                    if current_category is not None:
                        print()  # nowa linia między kategoriami
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
    # os.path.dirname(__file__) zwraca katalog, w którym znajduje się aktualny skrypt Python.
    # os.path.dirname(os.path.dirname(__file__)) dodatkowo przechodzi o jeden poziom wyżej, aby znaleźć katalog nadrzędny w stosunku do katalogu, w którym znajduje się skrypt Python.
    # os.path.join(..., 'car_rental') łączy ścieżkę do pliku db.sqlite3 w katalogu car_rental.
    db_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')
    show_offer(db_file)

if __name__ == "__main__":
    main()
