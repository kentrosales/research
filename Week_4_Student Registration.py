registration_counter = 50000
from datetime import datetime

def student_registration():
    global registration_counter
    while True:
        date= input("Enter the registration date (dd/mm/YY): ")
        try:
            date_entered = datetime.strptime(date, "%d%m%Y")
            if date_entered.year > 2026:
                print("Year cannot be beyond current year.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter date in the correct format.")
    while True:
        student_id = input("Enter Student ID: ")
        try:
            if len(student_id) != 4:
                print("Student ID must be up to 4 characters only.")
            else:
                break
        except ValueError:
            print("Invalid input. Please type correct format.")
        
        prefix = student_id[:2]
        suffix = student_id[2:4]

        if not prefix.isalpha:
            print("Error. First two characters must be letters.")
        elif not suffix.isnumeric:
            print("The last two characters should be numbers.")
        else:
            break

    while True:            
        student_name = input("Enter Student Name: ")
        try:
            if student_name.replace(" ", "").isalpha():
                break
            else:
                print("Name must be letters and spaces only.")
        except ValueError:
            print("Invalid input. Name must be letters and spaces only.")
            
    while True:
        course_name = input("Enter Course Name: ")
        try:
            if course_name.replace(" ", "").isalpha():
                break
            else:
                print("Please enter course name.")
        except ValueError:
            print("Invalid input. Course name must be letters and spaces only.")

    registration_counter += 1
    registration_id = registration_counter

    print("'Printing Student Information...'")
    print(f"Date: {date[:2]}/{date[2:4]}/{date[4:8]}")
    print(f"Student ID: ",(student_id).upper())
    print(f"Student Name: ",student_name.title())
    print(f"Course Name: ",course_name.upper())
    print(f"Registration ID: ",registration_id)

    return date, student_id, student_name, course_name, registration_id

student_details = student_registration()

