grade = int(input("Enter your grade: "))

if 0 <= grade <= 100:
    print("Valid grade:", grade)
else:
    print("Invalid grade. Grade must be between 0 and 100")