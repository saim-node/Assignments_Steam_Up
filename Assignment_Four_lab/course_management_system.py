# Initial courses dictionary
courses = {
    "Data Structures": {"Alice": 85, "Bob": 90, "Charlie": 75},
    "Algorithms": {"Alice": 95, "Dave": 88},
    "Machine Learning": {"Bob": 82, "Eve": 91, "Frank": 78}
}

#  : Update Data Structures course
courses["Data Structures"]["Alice"] = 90
courses["Data Structures"].pop("Charlie")

# Step 2: Add Web Development course
courses["Web Development"] = {
    "Grace": 92,
    "Henry": 85
}

#   Check and add Bob to Algorithms if needed
if "Bob" not in courses["Algorithms"]:
    courses["Algorithms"]["Bob"] = 80

#   Remove Machine Learning course
courses.pop("Machine Learning")

#  Calculate average grade for Data Structures
if "Data Structures" in courses:
    grades = courses["Data Structures"].values()
    average_grade = sum(grades) / len(grades)
else:
    average_grade = "Course not found"

# Display results
print("Updated Courses:", courses)
print("Average Grade in Data Structures:", average_grade)

