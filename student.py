students=[]
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    python = float(input("Enter Python marks: "))
    maths = float(input("Enter Maths marks: "))
    english = float(input("Enter English marks: "))

    student = {
        "name": name,"roll": roll,"python": python,"maths": maths,"english": english}
    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students)==0:
        print("NO students found.")
        return
print("/n=====STUDENT DETAILS=====")
for student in students:
    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("Python:", student["python"])
    print("Maths:", student["maths"])
    print("English:", student["english"])
    print("---------------------------")