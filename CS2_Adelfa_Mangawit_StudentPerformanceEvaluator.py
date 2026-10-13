#These are the global variables. Enter your inputs.

name = input("What is your name: ")
score1 = int(input("What is your score: "))
score2 = int(input("What is your score: "))
score3 = int(input("What is your score: "))
average = (score1 + score2 + score3) / 3

#This will display the title and separators (===)
def display_header():
    print("="*30)
    print("Student Performance Evaluator".center(30))
    print("="*30)

#This will print your student info and assessment scores which were your inputs you entered
def get_student_info():
    print(name)
    print(score1, score2, score3)

#This calculates your average and prints your average & performance level
def evaluate_performance():
    print(f"Average score: {average:.2f}")
    if average >= 90:
            print("Outstanding")
    elif average >= 85:
            print("Very Satisfactory")
    elif average >= 80:
            print("Satisfactory")
    elif average >= 75:
            print("Fairly Satisfactory")
    else:
        print("Needs Improvement")

def display_report():
    get_student_info()
    evaluate_performance()
display_header()
display_report()
