 attendance_list =[ ]
  
while True:
     name  = input("Enter student name :  ").strip().lower()
     
     if name in attendance_list :
         attendance_list.remove(name)
     elif name == "done":
         break 
     elif name == "":
         print("Invalid input. Please enter a valid student name or 'done' to finish.")
         continue
     else:
         attendance_list.append(name)
         
lent = len(attendance_list)         
if lent > 0 :
    print("  student names   " , attendance_list)
    
else:
    print( "No students were marked as present.  ")