books_file = 'books.txt'

def create_book_table():
    with open(books_file, 'w'):
        pass #just to make sure file exist

def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f"{name},{author},0\n")

def get_all_books():
    with open(books_file, 'r') as file:
        lines = [books.strip().split(',') for books in file.readlines()]

    return [{'name' : line[0],'author' : line[1],'read' : line[2]}
            for line in lines]

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

def list_books():
    print("List of books:")
    books = get_all_books()
    for book in books:
        print(f"Book name: {book['name']}, Author: {book['author']}, Read: {book['read']}")

def read_book(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read']  = 1
            break
    else:
        print(f"Book {name} is not found in database!")
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")