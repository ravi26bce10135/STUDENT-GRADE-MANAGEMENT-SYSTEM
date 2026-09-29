# Problem Statement

## Title
Student Grade Management System

## Problem
Teachers and small institutes often record student marks on paper or in scattered notes. This makes it slow to look up a student, calculate averages and grades, or find the top performer, and mistakes are easy to make. Data is also lost when it is not stored properly.

## Objective
Build a simple Python program that lets a user record, view, search, update and delete student marks, calculates averages and grades automatically, and keeps the data saved in a file between runs.

## Scope

**In scope**
- Console (text menu) based application
- Three subjects: Python, Maths, English
- Automatic average and grade calculation
- Permanent storage in a text file (`students.txt`)
- Basic CRUD operations: add, view, search, update, delete
- Finding the highest scorer

**Out of scope**
- Graphical or web interface
- Multiple user accounts or passwords
- Database systems
- Attendance, fees or timetable management

## Users
- **Teachers**: enter marks and check student performance
- **School / institute staff**: look up student results quickly
- **Students** (via a teacher): check their average and grade

## Features
1. **Add Student**: store name, roll number and marks in three subjects
2. **View Students**: list all student records
3. **Search Student**: find a student by roll number and show average and grade
4. **Find Highest Scorer**: show the student with the best average
5. **Update Student**: change a student's marks
6. **Delete Student**: remove a record
7. **File Storage**: save and load records automatically using `file_handler.py`

## Grading Rules

| Average | Grade |
|---------|-------|
| 90+ | A+ |
| 80-89 | A |
| 70-79 | B |
| 60-69 | C |
| 50-59 | D |
| Below 50 | F |

## Technology
- Language: Python 3
- Storage: plain text file (CSV format)
- Interface: command line

## Expected Outcome
A working program that manages student records reliably, gives correct grades, and keeps data safe between sessions.
