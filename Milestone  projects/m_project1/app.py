#project 1
#As a user, i should be able to do following:
#1. add new movies to my collection
#2.list all movies
#3. find a movie using movie title

#implementation
#data structure? list
#what data
#show user manual
#each requirement as a seperate fn
#quit type 'q'

MENU_PROMPT = "Enter 'a' to add a movie, 'l' to list movies, 'f' to find movie by title or 'q' to quit"
movies = []

def find():
    title = input("Enter movie title")
    for movie in movies:
        if movie['title'] == title:
            print(movie['title'], movie['director'], movie['year'])
            break
    else:
        print(f"No match found for title {title}")

def append():
    title = input("enter movie title")
    director = input("enter director name")
    year = input("enter year of release")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def list():
    for movie in movies:
        print(movie['title'], movie['director'], movie['year'])

user_options = {
    "a": append,
    "l": list,
    "f": find
}
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_fn = user_options[selection]
            selected_fn()
        else:
            print("Unknown input")
        selection = input(MENU_PROMPT)

menu()