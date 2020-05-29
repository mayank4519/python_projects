from utils import database

USER_CHOICE = """
Enter:
- 'a' : to add a new book
- 'l' : to list all books
- 'r' : to mark a book as read
- 'd' : to delete a book
- 'q' : quit application

Your choice:
"""

def prompt_add_book():
    name = input("Enter book name")
    author = input("Enter author name")
    database.add_book(name, author)

def prompt_list_books():
    database.list_books()

def prompt_read_books():
    name = input("Enter book name")
    database.mark_book_as_read(name)

def prompt_delete_books():
    name = input("Enter book name")
    database.delete_book(name)

user_options = {
    'a' : prompt_add_book,
    'l' : prompt_list_books,
    'r' : prompt_read_books,
    'd' : prompt_delete_books
}

def menu():
    database.create_book_table()
    user = input(USER_CHOICE)
    while user != 'q':
        if user in user_options:
            selected_fn = user_options[user]
            selected_fn()
        else:
            print(f"Invalid user input {user}.")

        user = input(USER_CHOICE)

menu()