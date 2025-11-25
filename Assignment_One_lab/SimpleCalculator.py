# Scenario Description:
# Create a simple calculator that asks the user to input two numbers,
# asks the user to choose an operation (Addition, Subtraction, Multiplication, Division),
# performs the chosen operation on the two numbers,
# and displays the result.
# Include error handling for division by zero (should avoid crashing and display an error message).

# Concepts Covered: User input, arithmetic operations, conditional logic.

# ============== Solution ================a

print("Welcome to Simlpe Calculator")

try:  
    num_1 = float(input("Enter number 1 :"))
    num_2 = float(input("Enter number 2 :"))
except ValueError:
    print("Invalid input! Please enter numeric values only.")
    exit() 
    
    
operation = input("Choose operation (+, -, *, /) :").strip()


# until funciton 
def opertaion(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation selected."
    
    
result = opertaion(operation, num_1, num_2)
print("The Result is :", result)

    