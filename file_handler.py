"""file_handler.py - Save and read student data for the Student Grade Management System.

Records are stored in students.txt, one student per line (CSV format):
    name,roll,python,maths,english
"""

import csv
import os

# Always look for students.txt next to this file, no matter where the program is run from
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")


def load_students():
    """Read all students from the file and return them as a list of dictionaries."""
    students = []

    if not os.path.exists(FILE_NAME):
        return students  # first run: no file yet

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 5:
                continue  # skip blank or damaged lines
            try:
                students.append({
                    "name": row[0],
                    "roll": row[1],
                    "python": float(row[2]),
                    "maths": float(row[3]),
                    "english": float(row[4]),
                })
            except ValueError:
                continue  # skip lines with invalid marks

    return students


def save_students(students):
    """Write the full list of students to the file (overwrites old content)."""
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for s in students:
            writer.writerow([s["name"], s["roll"], s["python"], s["maths"], s["english"]])
