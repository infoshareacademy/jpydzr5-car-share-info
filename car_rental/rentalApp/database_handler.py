import sqlite3
import uuid
import os

def get_db_file():
    """Returns the path to the SQLite database file."""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')

def connect_to_database():
    """Establishes a connection to the SQLite database and returns the connection object."""
    try:
        db_file = get_db_file()
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def close_database_connection(conn):
    """Closes the connection to the SQLite database."""
    try:
        if conn:
            conn.close()
    except sqlite3.Error as e:
        print(f"Error closing database connection: {e}")

def create_preorder(conn):
    try:
        cursor = conn.cursor()
        preorder_id = str(uuid.uuid4())  # Generate unique ID
        cursor.execute('INSERT INTO preorders (order_id, order_status) VALUES (?, ?)', (preorder_id, 'in_progress'))
        conn.commit()
        return preorder_id
    except sqlite3.Error as e:
        print(f"Error creating preorder: {e}")
        return None

def update_preorder(conn, preorder_id, column, value):
    try:
        cursor = conn.cursor()
        query = f'UPDATE preorders SET {column} = ? WHERE order_id = ?'
        cursor.execute(query, (value, preorder_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating preorder: {e}")

def confirm_preorder(conn, preorder_id):
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE preorders SET order_status = ? WHERE order_id = ?', ('confirmed', preorder_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error confirming preorder: {e}")


