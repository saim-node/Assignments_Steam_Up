
account_Details_input  = ""
while True:
    account_Details_input = input("Enter your 10 digit account number: ")
    if len(account_Details_input) == 10:
        print("Your complete account number is: ", account_Details_input) 
        break
    else:
        print("Invalid account number. Please enter a 10 digit account number.")


def account_Details(accountNumber):
        region = accountNumber[:3]
        branch = accountNumber[3:5]
        customer_number = accountNumber[5:]
    
        return region,branch,customer_number

user_account = account_Details(account_Details_input)
    
print( "The customer number is ",user_account[2])     
print( "The branch code is ",user_account[1])
print( "The region code is ",user_account[0])        