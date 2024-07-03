import sqlite3
from database_handler import connect_to_database, close_database_connection

def select_user():
    # Connect to the database
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, first_name, last_name FROM main.users")
        users = cursor.fetchall()
        if not users:
            print("Brak zarejestrowanych użytkowników.")
            return None

        print("Wybierz użytkownika:")
        for idx, user in enumerate(users):
            print(f"{idx + 1}. {user[1]} {user[2]}")  # user[1] - first_name, user[2] - last_name

        user_choice = int(input("Podaj numer użytkownika: "))
        if 1 <= user_choice <= len(users):
            selected_user = users[user_choice - 1]
            print(f"Wybrano użytkownika: {selected_user[1]} {selected_user[2]}")
            return selected_user
        else:
            print("Nieprawidłowy numer użytkownika. Spróbuj ponownie.")
            return None
    except ValueError:
        print("Nieprawidłowy numer użytkownika. Spróbuj ponownie.")
        return None
    finally:
        close_database_connection(conn)

def main():
    select_user()

if __name__ == "__main__":
    main()
