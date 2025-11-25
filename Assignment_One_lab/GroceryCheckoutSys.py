# Scenario Description
# You must design a basic grocery store checkout program. It should:
# Allow the user to enter the prices of three grocery items.
# Validate each price:
# No negative numbers
# No non-numeric input
# If invalid, ask again
# Calculate and display the total cost.
# Ask the user if they want to apply a membership discount.
# If they choose yes, apply a 10% discount to the total and display the new amount.

print("Welcome to the Grocery Store Checkout System!")
 
user_name = input("Enter Your Name :") 

items =1
total_price = 0

while items <= 3: 
    try:
        item_price = float(input(f'Enter the price of item {items}: '))
    except ValueError:
        print("Invalid input! Please Try Again \n")
        continue

    if item_price > 0 :
        total_price += item_price
        items +=1

    
print("The Total Amount is ",total_price)

membership = input("want to apply a membership discount type (y/n)").lower().strip()

if membership == "y":
    discount = total_price * 0.10  
    total_price = total_price - discount
    print("The Total Amount after applying for the membership is ",total_price)


print("---------------------------------------------------")
print("Thank You For Using Your Grocery System Hope You Liked it ") 

    

