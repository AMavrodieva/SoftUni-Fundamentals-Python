command = input()
courses = {}
while " : " in command:
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()
for course_name, student_name in courses.items():
    print(f'{course_name}: {len(student_name)}')
    for j in range(0, len(student_name)):
        print(f'-- {student_name[j]}')
