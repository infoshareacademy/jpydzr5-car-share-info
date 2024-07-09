import sqlite3

with sqlite3.connect("../db.sqlite3") as conn:
    cur = conn.cursor()
    cur.execute(
        """
        SELECT *
        FROM preorders p
        WHERE order_status = 'confirmed'
        ORDER BY id DESC
        LIMIT 1;
        """
    )

    # cur.execute("SELECT * FROM preorders")
    result = cur.fetchall()
    for row in result:
        print(row)
