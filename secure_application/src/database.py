import sqlite3

DB_NAME = "../outputs/library.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available INTEGER DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issued_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            issue_date TEXT,
            return_date TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_sample_books():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]

    if count == 0:
        books = [
            ("Python Programming", "John Smith"),
            ("Computer Networks", "Andrew Tanenbaum"),
            ("Operating Systems", "Abraham Silberschatz"),
            ("Database Management Systems", "Raghu Ramakrishnan"),
            ("Cryptography Basics", "William Stallings")
        ]

        cursor.executemany(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            books
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    add_sample_books()
    print("Database created successfully.")
