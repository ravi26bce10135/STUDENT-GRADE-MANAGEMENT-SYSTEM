import csv
import os

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")


def load_students():
    """Read all students from the file and return them as a list of dictionaries."""
    students = []

    if not os.path.exists(FILE_NAME):
        return students
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 5:
                continue
            try:
                students.append({"name": row[0],"roll": row[1],"python": float(row[2]),"maths": float(row[3]),"english": float(row[4]),})
            except ValueError:
                continue 
    return students


def save_students(students):
    """Write the full list of students to the file (overwrites old content)."""
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for s in students:
            writer.writerow([s["name"], s["roll"], s["python"], s["maths"], s["english"]])

def get_marks(subject):
    """Keep asking until a valid mark between 0 and 100 is entered."""
    while True:
        try:
            marks = float(input(f"Enter {subject} marks: "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def find_student(students, roll):
    """Return the student with this roll number, or None."""
    for student in students:
        if student["roll"] == roll:
            return student
    return None

def calculate_average(student):
    total = student["python"] + student["maths"] + student["english"]
    return total / 3

def get_grade(average):
    if average >= 90:
        return "A+"
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


def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    if find_student(students, roll):
        print("A student with this roll number already exists.")
        return
    python = get_marks("Python")
    maths = get_marks("Maths")
    english = get_marks("English")

    students.append({"name": name,"roll": roll,"python": python,"maths": maths,"english": english,})
    save_students(students)
    print("Student added successfully!")

def view_students(students):
    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== STUDENT DETAILS =====")
    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll"])
        print("Python:", student["python"])
        print("Maths:", student["maths"])
        print("English:", student["english"])
        print("---------------------------")


def search_student(students):
    roll = input("Enter roll number to search: ")
    student = find_student(students, roll)
    if student is None:
        print("Student not found.")
        return

    average = calculate_average(student)
    print("\nStudent Found!")
    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("Python:", student["python"])
    print("Maths:", student["maths"])
    print("English:", student["english"])
    print("Average:", round(average, 2))
    print("Grade:", get_grade(average))


def update_student(students):
    roll = input("Enter roll number to update: ")
    student = find_student(students, roll)

    if student is None:
        print("Student not found.")
        return

    student["python"] = get_marks("new Python")
    student["maths"] = get_marks("new Maths")
    student["english"] = get_marks("new English")
    save_students(students)
    print("Student details updated successfully!")


def delete_student(students):
    roll = input("Enter roll number to delete: ")
    student = find_student(students, roll)
    if student is None:
        print("Student not found.")
        return
    students.remove(student)
    save_students(students)
    print("Student deleted successfully!")


def highest_scorer(students):
    if len(students) == 0:
        print("No students found.")
        return

    highest = max(students, key=calculate_average)
    average = calculate_average(highest)

    print("\n===== HIGHEST SCORER =====")
    print("Name:", highest["name"])
    print("Roll Number:", highest["roll"])
    print("Average:", round(average, 2))
    print("Grade:", get_grade(average))
students = load_students()

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
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        highest_scorer(students)
    elif choice == "5":
        update_student(students)
    elif choice == "6":
        delete_student(students)
    elif choice == "7":
        print("Thank you for using STUDENT GRADE MANAGEMENT SYSTEM")
        break
    else:
        print("Invalid choice. Please try again.")

