cart_items = {
    "Laptop": "799.99",
    "Mouse": "25.50",
    "Keyboard": "45.00",
    "Headphones": "89.99"
}

subtotal = 0.0
discount = 0.1  # 10%

print("Items in Cart:")
for item in cart_items:
    print(item, ": $", cart_items[item])
    price = float(cart_items[item])  
    subtotal += price

discount_amount = subtotal * discount
total = subtotal - discount_amount

print("-------- Summary --------")
print("Subtotal : $", round(subtotal, 2))
print("Discount : ", discount * 100, "%")
print("Total    : $", round(total, 2))
