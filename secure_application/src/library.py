import sqlite3
from datetime import date
import html

DB_NAME = "../outputs/library.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


# -------------------------------
# 1. MEMBER REGISTRATION
# -------------------------------
def register_member():
    name = input("Enter member name: ")
    email = input("Enter email: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO members (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()
    conn.close()

    print("Member registered successfully.")


# -------------------------------
# 2. BOOK SEARCH
# -------------------------------
def search_book():
    title = input("Enter book title to search: ")

    conn = connect_db()
    cursor = conn.cursor()

    # INTENTIONALLY VULNERABLE TO SQL INJECTION
    query = "SELECT * FROM books WHERE title LIKE '%" + title + "%'"
    cursor.execute(query)

    books = cursor.fetchall()

    if books:
        print("\nSearch Results:")
        for book in books:
            status = "Available" if book[3] else "Issued"
            print(
                "ID:", book[0],
                "| Title:", book[1],
                "| Author:", book[2],
                "| Status:", status
            )
    else:
        print("No books found.")

    conn.close()


# -------------------------------
# 3. ISSUE BOOK
# -------------------------------
def issue_book():
    # INTENTIONALLY NO AUTHENTICATION CHECK

    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM members WHERE id = ?",
        (member_id,)
    )

    member = cursor.fetchone()

    if not member:
        print("Member not found.")
        conn.close()
        return

    cursor.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    )

    book = cursor.fetchone()

    if not book:
        print("Book not found.")
        conn.close()
        return

    if book[3] == 0:
        print("Book is already issued.")
        conn.close()
        return

    cursor.execute(
        """
        INSERT INTO issued_books
        (book_id, member_id, issue_date)
        VALUES (?, ?, ?)
        """,
        (book_id, member_id, str(date.today()))
    )

    cursor.execute(
        "UPDATE books SET available = 0 WHERE id = ?",
        (book_id,)
    )

    conn.commit()
    conn.close()

    print("Book issued successfully.")


# -------------------------------
# 4. RETURN BOOK
# -------------------------------
def return_book():
    # INTENTIONALLY NO AUTHENTICATION CHECK

    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM issued_books
        WHERE member_id = ?
        AND book_id = ?
        AND return_date IS NULL
        """,
        (member_id, book_id)
    )

    record = cursor.fetchone()

    if not record:
        print("No active issue record found.")
        conn.close()
        return

    cursor.execute(
        """
        UPDATE issued_books
        SET return_date = ?
        WHERE id = ?
        """,
        (str(date.today()), record[0])
    )

    cursor.execute(
        "UPDATE books SET available = 1 WHERE id = ?",
        (book_id,)
    )

    conn.commit()
    conn.close()

    print("Book returned successfully.")


# -------------------------------
# 5. FINE CALCULATION
# -------------------------------
def calculate_fine():
    try:
        late_days = int(input("Enter number of late days: "))

        if late_days < 0:
            print("Invalid number of days.")
            return

        fine = late_days * 10

        print("Fine = Rs.", fine)

    except ValueError:
        print("Please enter a valid number.")


# -------------------------------
# XSS DEMONSTRATION
# -------------------------------
def generate_member_report():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    conn.close()

    with open("../outputs/members.html", "w") as file:
        file.write("<html><body>")
        file.write("<h1>Library Members</h1>")

        for member in members:
            # INTENTIONALLY VULNERABLE TO XSS
            file.write(
                "<p>Member: " + member[1] +
                " | Email: " + member[2] + "</p>"
            )

        file.write("</body></html>")

    print("Member report generated.")
    print("Open ../outputs/members.html in a browser.")


# -------------------------------
# MAIN MENU
# -------------------------------
def main():

    while True:

        print("\n====================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Register Member")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Calculate Fine")
        print("6. Generate Member HTML Report")
        print("7. Exit")
        print("====================================")

        choice = input("Enter choice: ")

        if choice == "1":
            register_member()

        elif choice == "2":
            search_book()

        elif choice == "3":
            issue_book()

        elif choice == "4":
            return_book()

        elif choice == "5":
            calculate_fine()

        elif choice == "6":
            generate_member_report()

        elif choice == "7":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
