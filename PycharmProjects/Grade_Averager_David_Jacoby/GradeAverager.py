#Grade Averager David Jacoby

gradeTotal = 0
accumulator = 0

print("Welcome to the Grade Averager!")

while True:
    grade = int(input("Please enter the grades you wish to average on a scale of 0-100. Type 999 when ready to exit."))

    if grade == 999:
        break

    elif grade >= 0 and grade <= 100:
        gradeTotal += grade
        accumulator += 1

    else:
        print("ERROR: number is not in range of 0-100 please try again.")

if accumulator > 0:
    gradeAverage = gradeTotal / accumulator

    if gradeAverage >= 90:
        letterGrade = "A"
    elif gradeAverage >= 80:
        letterGrade = "B"
    elif gradeAverage >= 70:
        letterGrade = "C"
    elif gradeAverage >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"

    print("")
    print("The letter grade average was " + letterGrade + " with " + str(int(gradeAverage)) + " points")
    print("")
    print("Thank you for using the grade averager!")

else:
    print("")
    print("Thank you for using the Grade Averager!")
