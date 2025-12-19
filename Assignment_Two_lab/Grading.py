 
students = []
 
while True:
    num_input = input("How many students do you want to enter? ").strip()
    if num_input.isdigit() and int(num_input) > 0:
        num_students = int(num_input)
        break
    else:
        print("Please enter a valid positive number.")
 
for i in range(1, num_students + 1):
    name = input(f"\nEnter the name of student {i}: ").strip()
    while name == "":
        print("Name cannot be empty.")
        name = input(f"Enter the name of student {i}: ").strip()
     
    while True:
        score_input = input(f"Enter the score for {name} (0-100): ").strip()
        if score_input.isdigit() and 0 <= int(score_input) <= 100:
            score = int(score_input)
            break
        else:
            print("Please enter a valid score between 0 and 100.")
 
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
 
    students.append([name, score, grade])
 
print("\n=== Student Grades ===")
print(f"{'Name':<20} {'Score':>6} {'Grade':>6}")
print("-" * 34)
for name, score, grade in students:
    print(f"{name:<20} {score:>6} {grade:>6}")
