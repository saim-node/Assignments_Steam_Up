
inventory = []

print("Welcome to my shop!")

user_input = input("Do you want to add inventory? (y/n): ").strip().lower()

if user_input == "y":
    while True:
        # Get item name
        name = input("Enter the name of the item (or type 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if name == "":
            print("Item name cannot be empty.")
            continue
         
        quantity_input = input(f"Enter the quantity for '{name}': ").strip()
        if not quantity_input.isdigit():
            print("Quantity must be a number.")
            continue
        quantity = int(quantity_input)
 
        found = False
        for item in inventory:
            if item[0].lower() == name.lower():
                item[1] += quantity
                found = True
                print(f"Updated '{name}' quantity to {item[1]}.")
                break

        if not found:
            inventory.append([name, quantity])
            print(f"Added '{name}' with quantity {quantity} to inventory.")

    # Display total inventory
    print("\n=== Total Inventory ===")
    print(f"{'Item':<20} {'Quantity':>8}")
    print("-" * 30)
    for item, quantity in inventory:
        print(f"{item:<20} {quantity:>8}")

else:
    print("No worries! Inventory not added.")
