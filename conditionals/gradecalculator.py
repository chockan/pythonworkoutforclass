def grade_calculator():
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = 'A'
    elif 80 <= marks < 90:
        grade = 'B'
    elif 70 <= marks < 80:
        grade = 'C'
    elif 60 <= marks < 70:
        grade = 'D'
    else:
        grade = 'F'
    
    print("Grade:", grade)

grade_calculator()
