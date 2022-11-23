command = input()
exam_result = {}
exam_submission = {}
while command != "exam finished":
    current_command = command.split("-")
    if len(current_command) > 2:
        username = current_command[0]
        cur_language = current_command[1]
        point = int(current_command[2])
        if cur_language != "banned":
            if cur_language not in exam_submission:
                exam_submission[cur_language] = 0
            exam_submission[cur_language] += 1
            if username not in exam_result:
                exam_result[username] = {'language': '', "points": 0}
                if point < exam_result[username]['points']:
                    continue
                else:
                    exam_result[username] = {'language': cur_language,  "points": point}
    else:
        exam_result.pop(current_command[0])
    command = input()
sorted_list = sorted(exam_result.items(), key=lambda kvp: (-kvp[1]['points'], kvp[0]))
print(f'Results:')
for username, value in sorted_list:
    print(f'{username} | {value["points"]}')
print(f'Submissions:')
sorted_exam_result = sorted(exam_submission.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for cur_language, value in sorted_exam_result:
    print(f'{cur_language} - {value}')
