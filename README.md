# Student Grade Management System

A simple console-based Python program to manage student records and grades. Data is saved to a text file, so it is still there the next time you run the program.

## Features

- Add a student (name, roll number, Python / Maths / English marks)
- View all students
- Search a student by roll number (shows average and grade)
- Find the highest scorer
- Update a student's marks
- Delete a student
- Automatic saving and loading of data (`students.txt`)

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Main program: menu and all student operations |
| `file_handler.py` | Saves and reads student data |
| `students.txt` | Stores student records (one per line) |
| `README.md` | Project overview and how to run it |
| `statement.md` | Problem statement, scope, users and features |

## Requirements

- Python 3.6 or newer
- No external libraries needed

## How to Run

1. Put all files in the same folder.
2. Open a terminal in that folder.
3. Run:

   ```
   python main.py
   ```

4. Choose an option from the menu (1-7).

## Grading Scale

| Average | Grade |
|---------|-------|
| 90 and above | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

## Data Format

Each line in `students.txt` is one student:

```
name,roll,python,maths,english
Aarav Sharma,101,85.0,90.0,78.0
```

The two sample records included can be deleted from the menu (option 6) or by clearing the file.

## Sample Menu

```
===== STUDENT GRADE MANAGEMENT SYSTEM =====
1. Add Student
2. View Students
3. Search Student
4. Find Highest Scorer
5. Update Student
6. Delete Student
7. Exit
```

## Possible Future Improvements

- Add more subjects
- Sort students by marks
- Export a report card
- Add a graphical interface
