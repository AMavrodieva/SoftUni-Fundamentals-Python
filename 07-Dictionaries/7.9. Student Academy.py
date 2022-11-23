number_of_rows = int(input())
grades = {}
for number in range(0, number_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in grades:
        grades[student_name] = []
    grades[student_name].append(grade)

for student_name, grade in grades.items():
    number_of_grades = int(len(grade))
    average_grade = sum(grade) / number_of_grades
    if average_grade >= 4.50:
        print(f'{student_name} -> {average_grade:.2f}')
