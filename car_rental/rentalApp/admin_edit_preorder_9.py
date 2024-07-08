import sqlite3
from datetime import datetime, timedelta
from database_handler import connect_to_database, close_database_connection

def get_preorders():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT p.* FROM main.preorders p WHERE p.order_status = 'confirmed'")
    preorders = cursor.fetchall()
    close_database_connection(conn)
    return preorders

def display_preorders(preorders):
    if not preorders:
        print("Brak potwierdzonych zamówień.")
        return None

    print("Wybierz zamówienie:")
    for idx, preorder in enumerate(preorders):
        print(f"{idx + 1}. {preorder[1]}")

    return preorders

def get_preorder_choice(preorders):
    try:
        preorders_choice = int(input("Podaj numer zamówienia: "))
        if 1 <= preorders_choice <= len(preorders):
            selected_preorder = preorders[preorders_choice - 1]
            selected_preorder_id = selected_preorder[0]
            selected_preorder_number = selected_preorder[1]
            print(f"Wybrano zamówienie: {selected_preorder_number}")
            return selected_preorder_id
        else:
            print("Nieprawidłowy numer zamówienia. Spróbuj ponownie.")
            return None
    except ValueError:
        print("Nieprawidłowy numer zamówienia. Spróbuj ponownie.")
        return None

def get_date_input(prompt):
    try:
        date = input(prompt)
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        if date_obj < datetime.now().date():
            raise ValueError
        return date_obj
    except ValueError:
        print("Nieprawidłowy format daty lub data przeszła. Spróbuj ponownie.")
        return None

def get_time_input(prompt):
    try:
        time = input(prompt)
        time_obj = datetime.strptime(time, "%H:%M").time()
        if not datetime.strptime("06:00", "%H:%M").time() <= time_obj <= datetime.strptime("23:00", "%H:%M").time():
            raise ValueError
        return time_obj
    except ValueError:
        print("Nieprawidłowy format godziny lub godzina poza zakresem. Spróbuj ponownie.")
        return None

def update_preorder(preorder_id, start_date, start_time, end_date, end_time):
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        query = """
            UPDATE main.preorders
            SET order_start_date = ?, order_start_time = ?, order_end_date = ?, order_end_time = ?
            WHERE id = ? AND order_status = 'confirmed'
        """
        cursor.execute(query, (start_date, start_time, end_date, end_time, preorder_id))
        conn.commit()
        print("Zamówienie zostało zaktualizowane pomyślnie.")
    except sqlite3.Error as e:
        print(f"Error updating preorder: {e}")
    finally:
        close_database_connection(conn)

def select_preorder():
    preorders = get_preorders()
    if not preorders:
        return

    display_preorders(preorders)
    selected_preorder_id = get_preorder_choice(preorders)
    if not selected_preorder_id:
        return

    start_date = None
    while not start_date:
        start_date = get_date_input("Podaj nową datę rozpoczęcia wynajmu (YYYY-MM-DD): ")

    start_time = None
    while not start_time:
        start_time = get_time_input("Podaj nową godzinę odbioru (format HH:MM, między 06:00 a 23:00): ")

    end_date = None
    while not end_date:
        end_date = get_date_input("Podaj nową datę zakończenia wynajmu (YYYY-MM-DD): ")

    end_time = None
    while not end_time:
        end_time = get_time_input("Podaj nową godzinę zwrotu (format HH:MM, między 06:00 a 23:00): ")

    min_rent_date = timedelta(days=1)
    diff_rent_date = end_date - start_date

    if start_date >= end_date:
        print("Data zwrotu nie może być taka sama lub wcześniejsza od daty wynajmu.")
        return
    elif diff_rent_date <= min_rent_date:
        print("Czas wynajmu nie może być krótszy niż 1 dzień.")
        return

    start_date = start_date.strftime("%Y-%m-%d")
    start_time = start_time.strftime("%H:%M")
    end_date = end_date.strftime("%Y-%m-%d")
    end_time = end_time.strftime("%H:%M")

    update_preorder(selected_preorder_id, start_date, start_time, end_date, end_time)

def main():
    select_preorder()

if __name__ == "__main__":
    main()
