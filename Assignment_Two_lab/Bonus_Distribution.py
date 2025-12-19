data = [["Alice", 5], ["Bob", 4], ["Charlie", 3], ["David", 2], ["Eve", 5]]
new_list = []  
def calculate_bonus(data):
    for employee in data:
        name = employee[0]
        rating = employee[1]
    
        if rating == 5:
            bonus = 1000
        elif rating == 4:
            bonus = 750
        elif rating == 3:
            bonus = 500
        else:
            bonus = 0           
           
       
        new_list.append([name,rating,bonus])      
    return new_list          

bonuses = calculate_bonus(data)

for i in bonuses:
    print(f"Employee: {i[0]}, Rating: {i[1]}, Bonus: ${i[2]}")
