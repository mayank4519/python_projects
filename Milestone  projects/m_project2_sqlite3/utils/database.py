from .database_connection import DatabaseConnection

def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO books VALUES(?,?,0)',(name,author))

def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')

        # fetchall() return list of tuples but will convert into dictionary using list comprehension
        # [(name,author,read),(name,author,read)]
        books = [{'name' : row[0], 'author' : row[1], 'read' : row[2]} for row in cursor.fetchall()]

    return books

def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        books = get_all_books()
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))

def list_books():
    print("List of books:")
    books = get_all_books()
    for book in books:
        print(f"Book name: {book['name']}, Author: {book['author']}, Read: {book['read']}")

def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read = 1 WHERE name=?', (name,))