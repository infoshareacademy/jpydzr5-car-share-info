import sqlite3

# Compact, Economy, Medium, Mini, SUV


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
            1: "Compact",
            2: "Economy",
            3: "Medium",
            4: "Mini",
            5: "SUV",
        }

        category = int(row[2])
        if category in data.keys():
            category = data[category]

    return f"Twoja rezerwacja zaczyna się {row[0]} o godzinie {row[1]}. Wybrana kategoria samochodu to {category}. "


def main():
    print(summary())


if __name__ == "__main__":
    main()
