def add_book(library:dict, title:str, author:str, isbn:str):

    if isbn in library:
        print("Book already exists in the library.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }
        print("Book have been added successfully.")

def remove_book(library:dict, isbn:str):

    if isbn not in library:
        print("Book does not exist in the library.")
    else:
        del library[isbn]
        print("Book have been removed successfully.")

def check_out_book(library:dict, isbn:str):

    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available'] = False
            print("Book checked out successfully.")
        else:
            print("Book is already checked out.")
    else:
        print("Book does not exist in the library.")

def return_book(library:dict, isbn:str):

    if isbn in library:
        if not library[isbn]['available']:
            library[isbn]['available'] = True
            print("Book returned successfully, thank you.")
        else:
            print("Book is already in the library.")
    else:
        print("This book does not belong to this library.")

def display_books(library:dict):

    for i, isbn in enumerate(library, start= 1):

        book = library[isbn]
        print("-" * 50)
        print(f"#{i}:")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Availability: {book['available']}")