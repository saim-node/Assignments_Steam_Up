# Initial inventory
inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}

# Update stock for Smartphone and Headphones
inventory.update({
    "Smartphone": inventory["Smartphone"] + 10,
    "Headphones": inventory["Headphones"] + 5
})

#   Sell the last item added
sold_item = inventory.popitem()

#    Check stock for Camera
camera_stock = inventory.get("Camera", "Out of Stock")

# Display results
print("Updated Inventory:", inventory)
print("Sold Item:", sold_item)
print("Camera Stock Status:", camera_stock)
