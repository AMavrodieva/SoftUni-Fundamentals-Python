command = input()
exam_result = {}
exam_submission = {}
while command != "exam finished":
    current_command = command.split("-")
    try:
        if len(current_command) > 2:
            username = current_command[0]
            cur_language = current_command[1]
            point = int(current_command[2])
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
            username = current_command[0]
            exam_result.pop(username)
    except KeyError:
        print('error')
    command = input()
print(f'Results:')
for username, value in exam_result.items():
    print(f'{username} | {value["points"]}')
print(f'Submissions:')
for cur_language, value in exam_submission.items():
    print(f'{cur_language} - {value}')
