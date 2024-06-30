import os
import sqlite3

def connect_to_database(db_file):
    """ Establishes a connection to the SQLite database and returns the connection object """
    conn = sqlite3.connect(db_file)
    return conn

def fetch_extras_data(db_file):
    conn = connect_to_database(db_file)

    try:
        cursor = conn.cursor()
        query = """
            SELECT 
                e.extra_id AS id,
                e.name AS name,
                e.description AS description,
                e.price AS price
            FROM extras e
        """
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return []

def choose_extras(db_file) -> str | bool:
    # Fetch extras data from the database
    extras = fetch_extras_data(db_file)
    if not extras:
        return False

    print("[9/20] Dostępne dodatki:")
    for i, extra in enumerate(extras, start=1):
        print(f"{i}. {extra[2]}: {extra[3]:.2f}$ jednorazowo na cały okres najmu")

    try:
        choices = input("Wybierz dodatki (podaj numery po przecinku): ")
        choice_list = [int(choice.strip()) for choice in choices.split(",")]

        selected_ids = []
        selected_descriptions = []
        for choice in choice_list:
            if 1 <= choice <= len(extras):
                selected_extra = extras[choice - 1]
                selected_ids.append(str(selected_extra[0]))
                selected_descriptions.append(f"{selected_extra[2]} ({selected_extra[3]}$)")
            else:
                raise ValueError(f"Nieprawidłowy wybór: {choice}")

        # Passing ids numbers from the extras table
        result = ";".join(selected_ids)

        # Showing the descriptions from the extras table
        print(f"Wybrano dodatki: {', '.join(selected_descriptions)}")
        return result

    except ValueError as ve:
        print(f"Błąd: {ve}. Spróbuj ponownie.")
        return False


def main():
    # os.path.dirname(__file__)
    #  - returns the directory where the current Python script is located.
    # os.path.dirname(os.path.dirname(__file__))
    #  - goes one level up to find the parent directory relative to the directory where the Python script is located.
    # os.path.join(..., 'car_rental')
    #  - combines the path to the db.sqlite3 file in the car_rental directory.

    db_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')

    choose_extras(db_file)


if __name__ == "__main__":
    main()
