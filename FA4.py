num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

class_total = 0  

print()

for student in range(1, num_students + 1):
    print(f"Student {student}")
    student_total = 0
    
    for subject in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        student_total += score
    
    student_average = student_total / num_subjects
    print(f"Average for Student {student} = {student_average}\n")
    
    class_total += student_average

class_average = class_total / num_students
print(f"Class Average = {class_average}")