from connection import get_connection


# ------------------------------
# Books
# ------------------------------
def insert_book(book: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books (title, price, rating) VALUES (%s, %s, %s)",
        (
            book["title"],
            book["price"],
            book["rating"],
        )
    )

    conn.commit()
    cursor.close()
    conn.close()


def get_books():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, price, rating FROM books")
    rows = cursor.fetchall()

    books = []
    for row in rows:
        books.append({
            "id": row["id"],
            "title": row["title"],
            "price": row["price"],
            "rating": row["rating"],
        })

    cursor.close()
    conn.close()
    return books


# ------------------------------
# Users
# ------------------------------
def get_user(username: str):
    print('connecting to DB')
    conn = get_connection()
    print("connected to DB")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username, password, is_admin FROM users WHERE username = %s",
        (username,)
    )

    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        return None

    return {
        "id": row["id"],
        "username": row["username"],
        "password": row["password"],
        "is_admin": row["is_admin"],
    }


def create_user(username: str, password: str, is_admin: bool = False):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password, is_admin) VALUES (%s, %s, %s)",
        (username, password, is_admin)
    )

    conn.commit()
    cursor.close()
    conn.close()
