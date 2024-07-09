import sqlite3


def summary():
    with sqlite3.connect("../db.sqlite3") as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT order_start_date, order_start_time, order_car_category, order_extras
            FROM preorders p
            WHERE order_status = 'confirmed'
            ORDER BY id DESC
            LIMIT 1;
            """
        )

        result = cur.fetchall()
        for row in result:
            pass

        data = {
            1: "Mini",
            2: "Economy",
            3: "Compact",
            4: "SUV",
            5: "Medium",
        }

        cur.execute(
            """
            SELECT brand, model, license_plate_number, status
            FROM "cars"
            WHERE car_category = ?
            ORDER BY car_id DESC
            LIMIT 1;
            """,
            (row[2],),
        )

        result = cur.fetchall()
        for car_row in result:
            pass

    return f"Twoja rezerwacja zaczyna się {row[0]} o godzinie {row[1]}. Wybrana kategoria samochodu to {data[int(row[2])]}. \nPrzypisany samochód to {car_row[0]} {car_row[1]} z numerem rejestracyjnym {car_row[2]}."


def main():
    print(summary())


if __name__ == "__main__":
    main()
