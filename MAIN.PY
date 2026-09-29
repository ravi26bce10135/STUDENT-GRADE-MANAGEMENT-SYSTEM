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

def calculate_average(student):
    total = student["python"] + student["maths"] + student["english"]
    average = total / 3
    return average

def get_grade(average):
    if average >=90:
        return"A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            average = calculate_average(student)
            grade = get_grade(average)

            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll"])
            print("Python:", student["python"])
            print("Maths:", student["maths"])
            print("English:", student["english"])
            print("Average:", round(average, 2))
            print("Grade:", grade)
            return
        print("Student not found.")

def highest_scorer():
    if len(students) == 0:
        print("No students found.")
        return
    highest = students[0]

    for student in students:
        if calculate_average(student) > calculate_average(highest):
            highest = student

    average = calculate_average(highest)

    print("\n===== HIGHEST SCORER =====")
    print("Name:", highest["name"])
    print("Roll Number:", highest["roll"])
    print("Average:", round(average, 2))
    print("Grade:", get_grade(average))

def update_student():
    roll = input("Enter roll no to update:")
    for student in students:
        if student["roll"] == roll:
            student["python"]=int(input("enter new python marks:"))
            student["maths"]=int(input("enter new maths marks:"))
            student["english"]=int(input("enter new english marks:"))
            print("Student details updated sucessfully")
            return
        print("student not found")

def delete_student():
    roll = input("Enter roll no to delete:")
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("student deleted successfully")
            return
        print("student not found.")

while True:
    print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Find Highest Scorer")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        highest_scorer()

    elif choice == "5":
        update_student()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        print("Thank you for using STUDENT GRADE MANAGEMENT SYSTEM")
        break

    else:
        print("Invalid choice. Please try again.")

