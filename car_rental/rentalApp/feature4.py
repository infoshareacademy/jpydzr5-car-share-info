from database_handler import connect_to_database, close_database_connection


def fetch_extras_data():
    conn = connect_to_database()

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
    finally:
        close_database_connection(conn)


def choose_extras() -> str | bool:
    # Fetch extras data from the database
    extras = fetch_extras_data()
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
    choose_extras()


if __name__ == "__main__":
    main()
