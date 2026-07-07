"""
Final Python Lab: Student Grade Analyzer
Student Version Starter Code

"""

import csv
import matplotlib.pyplot as plt


CSV_FILE = "students.csv"
REPORT_FILE = "grade_report.txt"


def read_students(filename):
    """
    Read student data from a CSV file.

    Expected return value:
    A list of dictionaries.
    """

    students = []

    # Open CSV file
    with open(filename, "r") as file:

        # Read rows using DictReader
        reader = csv.DictReader(file)

        for row in reader:

            # Convert score to integer
            student = {
                "name": row["name"],
                "student_id": row["student_id"],
                "score": int(row["score"])
            }

            students.append(student)

    return students


def calculate_statistics(students):
    """
    Calculate basic statistics.
    """

    stats = {}

    # Get all scores
    scores = []

    for student in students:
        scores.append(student["score"])

    # Calculate statistics
    total_students = len(scores)
    average_score = round(sum(scores) / total_students, 2)
    highest_score = max(scores)
    lowest_score = min(scores)

    # Count pass and fail students
    pass_count = 0
    fail_count = 0

    for score in scores:

        if score >= 60:
            pass_count += 1
        else:
            fail_count += 1

    # Store values in dictionary
    stats["total_students"] = total_students
    stats["average_score"] = average_score
    stats["highest_score"] = highest_score
    stats["lowest_score"] = lowest_score
    stats["pass_count"] = pass_count
    stats["fail_count"] = fail_count

    return stats


def get_grade(score):
    """
    Convert a numeric score to a letter grade.
    """

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    else:
        return "F"


def add_grades(students):
    """
    Add a grade field to each student dictionary.
    """

    for student in students:

        grade = get_grade(student["score"])

        # Add grade to dictionary
        student["grade"] = grade

    return students


def count_grade_distribution(students):
    """
    Count how many students received each grade.
    """

    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for student in students:

        grade = student["grade"]

        distribution[grade] += 1

    return distribution


def print_summary(stats, distribution):
    """
    Print the analysis result on the screen.
    """

    print("Student Grade Analyzer")
    print("----------------------")

    print("Total students:", stats["total_students"])
    print("Average score:", stats["average_score"])
    print("Highest score:", stats["highest_score"])
    print("Lowest score:", stats["lowest_score"])
    print("Passing students:", stats["pass_count"])
    print("Failing students:", stats["fail_count"])

    print("\nGrade Distribution:")

    for grade, count in distribution.items():
        print(grade + ":", count)


def write_report(filename, stats, distribution):
    """
    Write the analysis result to a text file.
    """

    with open(filename, "w") as file:

        file.write("Student Grade Analyzer\n")
        file.write("----------------------\n")

        file.write(f"Total students: {stats['total_students']}\n")
        file.write(f"Average score: {stats['average_score']}\n")
        file.write(f"Highest score: {stats['highest_score']}\n")
        file.write(f"Lowest score: {stats['lowest_score']}\n")
        file.write(f"Passing students: {stats['pass_count']}\n")
        file.write(f"Failing students: {stats['fail_count']}\n")

        file.write("\nGrade Distribution:\n")

        for grade, count in distribution.items():
            file.write(f"{grade}: {count}\n")


def create_chart(distribution):
    """
    Create a bar chart for grade distribution.
    """

    grades = list(distribution.keys())
    counts = list(distribution.values())

    plt.figure(figsize=(7, 5))

    plt.bar(grades, counts)

    plt.title("Grade Distribution")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")

    # Save chart
    plt.savefig("grade_chart.png")

    # Show chart on screen
    plt.show()


def main():
    """
    Main program workflow.
    """

    students = read_students(CSV_FILE)

    stats = calculate_statistics(students)

    students = add_grades(students)

    distribution = count_grade_distribution(students)

    print_summary(stats, distribution)

    write_report(REPORT_FILE, stats, distribution)

    create_chart(distribution)

    print("\nReport generated:", REPORT_FILE)
    print("Chart generated: grade_chart.png")


if __name__ == "__main__":
    main()