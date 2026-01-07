
inventory = ()
tuple_len = 0

while tuple_len < 5:
    fruit = input("Enter the fruit name: ").strip().lower()
    
    if fruit == "" or not fruit.isalpha():
        print("Invalid input! Please enter a valid fruit name.")
    else:
        inventory += (fruit,)
        tuple_len += 1
        print(f"Added '{fruit}' to inventory. Current inventory: {inventory}")

print("\nInventory is full (5 fruits).")
print("You can now update the inventory by removing a fruit and adding a new one.")
print("------------------ Current Inventory ------------------")
print(inventory)

while True:
    choice = input("\nType 'y' to continue updating, 'n' to stop: ").strip().lower()
    
    if choice == "y":
        fruit_to_remove = input("Enter the fruit name you want to remove: ").strip().lower()
        
        if fruit_to_remove in inventory:
            temp_list = list(inventory)
            temp_list.remove(fruit_to_remove)
            
            fruit_to_add = input("Enter the new fruit name to add: ").strip().lower()
            
            if fruit_to_add != "" and fruit_to_add.isalpha():
                temp_list.append(fruit_to_add)
                inventory = tuple(temp_list)
                print(f"Updated inventory: {inventory}")
            else:
                print("Invalid input! Please enter a valid fruit name to add.")
        else:
            print(f"'{fruit_to_remove}' not found in inventory.")
            
    elif choice == "n":
        print("Stopping the update process.")
        break
    else:
        print("Invalid choice! Please type 'y' or 'n'.")

print("\n----------- FINAL INVENTORY --------------")
print(inventory)