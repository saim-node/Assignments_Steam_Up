
books = ["rich dad poor dad", "the intelligent investor", "think and grow rich"]

books = [book.strip().lower() for book in books]

print("------------Available Books:-----------")
for book in books:
    print(book)

def add_book(book_name):
    book_name = book_name.strip().lower()
    if book_name in books:
        print("The book is already available.")
    else:
        books.append(book_name)
        print("Book added successfully!")

def remove_book(book_name):
    book_name = book_name.strip().lower()
    if book_name in books:
        books.remove(book_name)
        print("Book removed successfully!")
    else:
        print("Book name didn't match any available book.")

def find_book(book_name):
    book_name = book_name.strip().lower()
    if book_name in books:
        print("This book is available in the library.")
    else:
        print("Book not found.")


while True:
    user_input = input("\nEnter the book name: ").strip()
    
    if user_input == "":
        print("Invalid input! Please try again.")
    else:
        break

add_option = input("Do you want to add this book? (y/n): ").strip().lower()
if add_option == "y":  
    add_book(user_input)

remove_option = input("Do you want to remove this book? (y/n): ").strip().lower()
if remove_option == "y":
    remove_book(user_input)

find_option = input("Do you want to find this book? (y/n): ").strip().lower()
if find_option == "y":
    find_book(user_input)

print("\n------------Final Available Books:-----------")
for book in books:
    print(book)
