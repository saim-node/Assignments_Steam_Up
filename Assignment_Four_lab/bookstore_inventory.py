# Initial books dictionary
books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}

#   Create a backup copy
books_backup = books.copy()

#   Print all book titles and prices
print("Current Inventory:")
for title, price in books.items():
    print(title, ":", price)

# Calculate total value of books
total_value = sum(books.values())
print("\nTotal value of books:", total_value)

#   Remove sold book
sold_price = books.pop("1984")
print("\nSold Book: 1984")
print("Price:", sold_price)

# Display updated inventory
print("\nUpdated Inventory:", books)
