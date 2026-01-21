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
            "id": row[0],
            "title": row[1],
            "price": row[2],
            "rating": row[3],
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
        "SELECT id, username, password, role FROM users WHERE username = %s",
        (username,)
    )
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        return None


    return {
        "id": row[0],
        "username": row[1],
        "password": row[2],
        "role": row[3],
    }


def create_user(username: str, password: str, role: str = False):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
        (username, password, role)
    )

    conn.commit()
    cursor.close()
    conn.close()


print("CURD module loaded")