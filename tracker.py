# Name: SAKSHAM SHARMA
# Date: 11/11/25
# Assignment Title: Student Attendance Tracker

from datetime import datetime

def line():
    print("=" * 60)

print(" Welcome to Student Attendance System ")
line()
print("This system helps you record student's names along with their check-in time, prevents duplicate entries, and shows a summary automatically.")
line()
print()

# ask for total number of students
total_count = input("Enter total number of attendees: ")

while not total_count.isdigit() or int(total_count) <= 0:
    line()
    print(" Please enter a valid positive number.")
    line()
    total_count = input("Enter total number of attendees: ")

total_count = int(total_count)
line()

attendance = {}

for slot in range(1, total_count + 1):
    while True:
        student = input(f"Enter the name of {slot} student: ").strip()

        if student == "":
            line()
            print("Name field cannot be empty, Please enter again.")
            line()
            continue

        # input check-in time
        check_time = input("Enter check-in time (e.g. 09:30 AM): ").strip()
        while check_time == "":
            line()
            print(" Time field is *required*, Please re-enter.")
            line()
            check_time = input("Enter check-in time (e.g. 09:30 AM): ").strip()

        line()

        # if student already present in the dictionary
        if student not in attendance:
            attendance[student] = check_time
            break
        else:
            line()
            print(f" {student} is already marked present.")
            line()
            continue

print()
line()
print("Name of Student\t\tCheck-In Time")
line()

for person, timing in attendance.items():
    print(f"{person}\t\t\t{timing}")

line()
print(f"Total Students Present: {len(attendance)}")
line()

choices = input('Do you want to save the data? Enter "Y" for Yes or "N" for No: ').strip().upper()

if choices == "Y":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("attendance_log.txt", "w") as f:
        f.write("=" * 60 + "\n")
        f.write(f"Attendance Report Generated On: {timestamp}\n")
        f.write("=" * 60 + "\n")
        f.write("Name of Student\t\tCheck-In Time\n")
        f.write("=" * 60 + "\n")
        for person, timing in attendance.items():
            f.write(f"{person}\t\t{timing}\n")
        f.write("=" * 60 + "\n")
        f.write(f"Total Students Present: {len(attendance)}\n")
        f.write("=" * 60 + "\n")
    print(" Attendance successfully saved to 'attendance_log.txt'")
else:
    print(" Attendance not saved, Thank you for using the system!")
