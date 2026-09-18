# Name: Denver Ha
# Period: AM
# Student Performance Analyzer

# Intoduction to Program
print("========================================")
print("       STUDENT PERFORMANCE ANALYZER")
print("========================================")
print()
print("Enter the student's information below")

# Asking for student info
name = input("What is the student's name? ")
grade_level = int(input("What grade level is the student in? "))
assignment = float(input("What is the student's assignment average? "))
quiz = float(input("What is the student's quiz average? "))
test = float(input("What is the student's test average? "))
attendance = float(input("What is the student's attendance percentage? "))
missing = int(input("How many missing assignments does the student have? "))

# Function for calculating overall grade
def calculate_grade(assignment_average, quiz_average, test_average):
    overall_grade = assignment_average * .3 + quiz_average * .3 + test_average * .4
    return overall_grade

overall = calculate_grade(assignment, quiz, test)

# Function for calculating letter grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        return "A"
    elif overall_grade >= 80:
        return "B"
    elif overall_grade >= 70:
        return "C"
    elif overall_grade >= 60:
        return "D"
    else:
        return "F"

letter = letter_grade(overall)

# Function for attendance status
def attendance_status(attendance):
    if attendance >= 95:
        return "Excellent Attendance"
    elif attendance >= 90:
        return "Good Attendance"
    elif attendance >= 80:
        return "Attendance Warning"
    else:
        return "Poor Attendance"

attendance_state = attendance_status(attendance)

# Function for missing assignment status
def assignment_status(missing_assignments):
    if missing_assignments >= 5:
        return "Critical"
    elif missing_assignments >= 3:
        return "Warning"
    elif missing_assignments >= 1 :
        return "Good"
    else:
        return "Excellent"

missing_state = assignment_status(missing)

# Function for academic eligibility
def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Student passed all three requirements")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low")
    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low")

# Function for high honors check
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments")
        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met")
    else:
        print("High Honors: NO") 
        print("Reason: Grade requirement not met")

# Function for good standing
def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        print("Good Standing: YES")
    else:
        print("Good standing: NO")

# Function for academic support
def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")

# Asking for student login
username = input("Enter username: ")
pin = int(input("Enter PIN: "))
if username == "student":
    if pin == 1234:
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")
else:
    print("Login Failed: Incorrect username.")

# Function for grade level
def grade_level_message(grade_level):
    if grade_level == 9:
        print("Welcome to your freshman year!")
    elif grade_level == 10:
        print("Keep building your skills!")
    elif grade_level == 11:
        print("Junior year - keep")
    elif grade_level == 12:
        print("Senior year - finish strong!")
    else:
        print("Invalid grade level")

# Functino for strongest category
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average > quiz_average and assignment_average > test_average:
        print("Strongest Category: Assignments")
    elif quiz_average > assignment_average and quiz_average > test_average:
        print("Strongest Category: Quizzes")
    elif test_average > assignment_average and test_average > quiz_average:
        print("Strongest Category: Tests")
    else:
        print("No single strongest category")

# Function for advanced student (EXTRA CREDIT)
def check_advanced_status(grade, attendance, missing):
    if grade >= 90 and attendance >= 95 or grade >= 85 and missing == 0:
        print("OUTSTANDING STUDENT")
    else:
        print("STANDARD STUDENT STATUS")

# Final Student Summary
print("STUDENT SUMMARY")
print("---------------")
print("Student: " + name)
print("Grade Level: " + str(grade_level))
print()
print("Assignment Average: " + str(assignment))
print("Quiz Average: " + str(quiz))
print("Test Average: " + str(test))
print()
print("Attendance: " + str(attendance))
print("Missing Assignments: " + str(missing))
print()
print("Overall grade: " + str(overall))
print("Letter grade: " + letter)
print()
print("Attendance Status: " + attendance_state)
print("Assignment Status: " + missing_state)
print()
check_eligibility(overall, attendance, missing)
print()
check_high_honors(overall, attendance, missing)
print()
check_good_standing(overall, attendance)
print()
check_support(overall, attendance)
print()
strongest_category(assignment, quiz, test)
print()
check_advanced_status(overall, attendance, missing)
print()
grade_level_message(grade_level)

'''
========================================
       STUDENT PERFORMANCE ANALYZER
========================================

Enter the student's information below
What is the student's name? Denver Ha
What grade level is the student in? 12
What is the student's assignment average? 96
What is the student's quiz average? 99
What is the student's test average? 98
What is the student's attendance percentage? 98
How many missing assignments does the student have? 0
Enter username: student
Enter PIN: 1234
Login Successful!
STUDENT SUMMARY
---------------
Student: Denver Ha
Grade Level: 12

Assignment Average: 96.0
Quiz Average: 99.0
Test Average: 98.0

Attendance: 98.0
Missing Assignments: 0

Overall grade: 97.7
Letter grade: A

Attendance Status: Excellent Attendance
Assignment Status: Excellent

Academic Eligibility: ELIGIBLE
Student passed all three requirements

High Honors: YES

Good Standing: YES

Additional Support: NOT NEEDED

Strongest Category: Quizzes

OUTSTANDING STUDENT

Senior year - finish strong!
'''