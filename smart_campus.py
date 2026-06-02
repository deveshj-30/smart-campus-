import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "students.csv"


# -------------------------------
# Grade Evaluation
# -------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


# -------------------------------
# Fee Calculation
# -------------------------------
def calculate_fee(course):
    fees = {
        "Python": 15000,
        "Java": 18000,
        "AI": 25000,
        "Data Science": 30000
    }

    return fees.get(course, 10000)


# -------------------------------
# Student Registration
# -------------------------------
def register_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    grade = calculate_grade(marks)
    fee = calculate_fee(course)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, age, course, marks, grade, fee])

    print("Student Registered Successfully!")


# -------------------------------
# Display Records
# -------------------------------
def display_students():
    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No records found.")
        else:
            print("\nStudent Records")
            print(df)

    except FileNotFoundError:
        print("Record file not found.")


# -------------------------------
# Search Student
# -------------------------------
def search_student():
    student_id = input("Enter Student ID to Search: ")

    df = pd.read_csv(FILE_NAME)

    result = df[df["ID"].astype(str) == student_id]

    if len(result) > 0:
        print(result)
    else:
        print("Student not found.")


# -------------------------------
# Sort Student Records
# -------------------------------
def sort_students():
    df = pd.read_csv(FILE_NAME)

    print("\n1. Sort by Name")
    print("2. Sort by Marks")

    choice = input("Enter choice: ")

    if choice == "1":
        sorted_df = df.sort_values("Name")
    elif choice == "2":
        sorted_df = df.sort_values("Marks", ascending=False)
    else:
        print("Invalid Choice")
        return

    print(sorted_df)


# -------------------------------
# Course Enrollment
# -------------------------------
def course_enrollment():
    student_id = input("Enter Student ID: ")
    new_course = input("Enter New Course: ")

    df = pd.read_csv(FILE_NAME)

    index = df[df["ID"].astype(str) == student_id].index

    if len(index) > 0:
        df.loc[index, "Course"] = new_course
        df.loc[index, "Fee"] = calculate_fee(new_course)

        df.to_csv(FILE_NAME, index=False)

        print("Course Updated Successfully")
    else:
        print("Student Not Found")


# -------------------------------
# Directory Scanning
# -------------------------------
def scan_directory():
    path = input("Enter Directory Path: ")

    try:
        files = os.listdir(path)

        print("\nFiles in Directory:")
        for file in files:
            print(file)

    except FileNotFoundError:
        print("Directory does not exist.")

    except PermissionError:
        print("Permission Denied.")


# -------------------------------
# Student Analytics
# -------------------------------
def performance_analytics():
    try:
        df = pd.read_csv(FILE_NAME)

        marks = np.array(df["Marks"])

        print("\nAnalytics Report")
        print("Average Marks:", np.mean(marks))
        print("Highest Marks:", np.max(marks))
        print("Lowest Marks:", np.min(marks))

        plt.figure(figsize=(6, 4))
        plt.bar(df["Name"], df["Marks"])
        plt.title("Student Performance")
        plt.xlabel("Students")
        plt.ylabel("Marks")
        plt.show()

    except FileNotFoundError:
        print("No data file found.")

    except Exception as e:
        print("Error:", e)


# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n===== SMART CAMPUS INFORMATION SYSTEM =====")
        print("1. Register Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Sort Students")
        print("5. Course Enrollment")
        print("6. Directory Scan")
        print("7. Performance Analytics")
        print("8. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            sort_students()

        elif choice == "5":
            course_enrollment()

        elif choice == "6":
            scan_directory()

        elif choice == "7":
            performance_analytics()

        elif choice == "8":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()