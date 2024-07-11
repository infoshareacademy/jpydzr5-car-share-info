import sqlite3
from database_handler import connect_to_database, close_database_connection

def summary(conn, preorder_id):
    """Executes an SQL query and returns the results."""

    try:
        cursor = conn.cursor()
        query = """SELECT 
                        cc.description AS car_cat_description,
                        p.order_start_date AS start_date,
                        p.order_start_time AS start_time,
                        p.order_end_date AS end_date,
                        p.order_end_time AS end_time,
                        p.order_car_category AS car_cat,
                        cc.price AS car_cat_price,
                        p.order_extras AS extras,
                        JULIANDAY(p.order_end_date) - JULIANDAY(p.order_start_date) AS days_diff,
                        (JULIANDAY(p.order_end_date) - JULIANDAY(p.order_start_date)) * cc.price AS total_price
                    FROM preorders p
                    LEFT JOIN car_categories cc ON cc.cat_id = p.order_car_category 
                    WHERE p.order_id = ?
                """
        cursor.execute(query, (preorder_id,))
        result = cursor.fetchone()

        if not result:
            return "No matching preorder found."

        car_cat_description, order_start_date, order_start_time, order_end_date, order_end_time, order_car_category, car_cat_price, order_extras, days_diff, total_price = result

        # Oblicz cenę dla dodatków
        extras_price = 0
        if order_extras:
            extras = order_extras.split(";")
            for extra_id in extras:
                extra_query = """SELECT price, price_unit
                                 FROM extras
                                 WHERE extra_id = ?"""
                cursor.execute(extra_query, (extra_id,))
                extra_result = cursor.fetchone()
                if extra_result:
                    extra_price, price_unit = extra_result
                    if price_unit == "per_day":
                        extras_price += extra_price * days_diff
                    elif price_unit == "per_rental":
                        extras_price += extra_price
        total_car_price = total_price
        total_price += extras_price

        result = {
            "description": car_cat_description,
            "start_date": order_start_date,
            "start_time": order_start_time,
            "end_date": order_end_date,
            "end_time": order_end_time,
            "car_category": order_car_category,
            "car_category_price": car_cat_price,
            "total_car_price": total_car_price,
            "extras": order_extras,
            "days_diff": days_diff,
            "extras_price": extras_price,
            "total_price": total_price
        }
        if result:
            # Formatowanie danych
            formatted_car_cat_price = f"{result['car_category_price']:.2f}$"
            formatted_extras_price = f"{result['extras_price']:.2f}$"
            formatted_total_car_price = f"{result['total_car_price']:.2f}$"
            formatted_total_price = f"{result['total_price']:.2f}$"

            # Drukowanie sformatowanych danych
            print(f"Twoja rezerwacja zaczyna się {result['start_date']} o godzinie {result['start_time']}. \n"
                  f"Wybrana kategoria samochodu to {result['description']}. \n"
                  f"Cena wynajmu samochodu to {formatted_total_car_price} \n"
                  f"Cena wybranych dodatków to {formatted_extras_price} \n"
                  f"Łączna cena do zapłaty to {formatted_total_price}.")
        else:
            print("No matching preorder found.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        close_database_connection(conn)
        return None

def main():
    summary()

if __name__ == "__main__":
    main()
