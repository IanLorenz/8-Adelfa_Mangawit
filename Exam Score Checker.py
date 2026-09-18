try:
    examination_score = int(input("Enter examination score: "))
    print("Examination Score:", examination_score)

except ValueError:
    print("Invalid examination score. Enter a whole number.")

if 0 <= examination_score <= 100:
    print("Valid Examination Score:", examination_score)
else:
    print("Invalid Examination Score. Score m12ust be between 0 and 100.")