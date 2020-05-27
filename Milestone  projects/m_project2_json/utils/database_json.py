import json
books_file = 'books.json'

def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)

def add_book(name, author):
    books = get_all_books()
    books.append({'name':name, 'author': author, 'Read': False})
    _save_all_books(books)

def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

def list_books():
    print("List of books:")
    books = get_all_books()
    for book in books:
        print(f"Book name: {book['name']}, Author: {book['author']}, Read: {book['Read']}")

def read_book(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['Read']  = True
            break
    else:
        print(f"Book {name} is not found in database!")
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)