import re
student_id = input("Enter student ID: ")

pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern, student_id):
    print("Valid student ID")
else:
    print("Invalid student ID")