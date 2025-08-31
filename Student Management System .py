# Student Management System with File Storage

import os

FILE_NAME = "students_record.txt"

# Add a student record
def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll No: ")
    marks = []
    for i in range(1, 4):
        m = int(input(f"Enter Marks for Subject {i}: "))
        marks.append(m)

    avg = sum(marks) / 3
    grade = calculate_grade(avg)

    student = {
        "Name": name,
        "RollNo": roll_no,
        "Marks": marks,
        "Average": avg,
        "Grade": grade
    }

    with open(FILE_NAME, "a") as f:
        f.write(str(student) + "\n")

    print("Student record added successfully!\n")

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "Fail"


# View all student records
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            print(line.strip())

# Search student by Roll No
def search_student():
    roll_no = input("Enter Roll No to search: ")
    found = False
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            record = eval(line.strip())  # Convert string back to dictionary
            if record["RollNo"] == roll_no:
                print("Student Found:", record)
                found = True
                break
    if not found:
        print("Student not found.")

# Main menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student Record")
    print("2. View All Students Records")
    print("3. Search Student by Roll No")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")
