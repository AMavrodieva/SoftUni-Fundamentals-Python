data = input()
courses = {}
while ":" in data:
    name_student, id_student, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][id_student] = name_student
    data = input()
searched_course = data
searched_course_name_as_list = searched_course.split("_")
searched_course = " ".join(searched_course_name_as_list)

for course_name in courses:
    if course_name == searched_course:
        for id_student, name_student in courses[course_name].items():
            print(f"{name_student} - {id_student}")
