gpa = float(input("What was your grade point average? "))
lowest_grade = float(input("What was your lowest grade? "))

if gpa >= 0.85 and lowest_grade >= 0.70:
    honor_roll = True
else:
    honor_roll = False

if honor_roll:
    print("You won the honor roll")