import json
from library import librarian


def save_library(library:dict):
    with open("books.json", "w", encoding="UTF-8") as file:
        json.dump(library, file, indent=4)


try:
    with open("books.json", "r", encoding="UTF-8") as file:
        library = json.load(file)

except FileNotFoundError:
    library = {}


while True:

    print("-" * 50)
    print("Welcome to the library system ^_^")
    print("-" * 50)
    print("1. Add a book")
    print("2. Delete a book")
    print("3. Display all books")
    print("4. Search for a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("NOTE: To exit the system, enter -> exit")
    print("-" * 50)

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")  
        librarian.add_book(library, title, author, isbn)
        save_library(library)

    elif choice == '2':
        isbn = input("Enter ISBN: ")
        librarian.remove_book(library, isbn)
        save_library(library)

    elif choice == '3':
        librarian.display_books(library)

    elif choice == '4':
        isbn = input("Enter ISBN: ")

        if isbn in library:
            book = library[isbn]
            print("-" * 50)
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ISBN: {book['isbn']}")
            print(f"Availability: {book['available']}")
        else:
            print("Book does not exsit in this library.")

    elif choice == '5':
        isbn = input("Enter ISBN: ")
        librarian.check_out_book(library, isbn)
        save_library(library)

    elif choice == '6':
        isbn = input("Enter ISBN: ")
        librarian.return_book(library, isbn)
        save_library(library)

    elif choice.lower() == "exit":
        print("Thank you for using the library, see you soon. ^_^")
        break

    else:
        print("Enter a valid choice")