import re
text = input()
pattern = r"([|#])(?P<item>[A-Za-z\s]+)(\1)(?P<date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>\d+)(\1)"
#pattern = r"([|#])(?P<name>[A-Za-z\s]+)(\1)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(\1)(?P<calories>[0-9]+)(\1)"
valid_text = re.finditer(pattern, text)
food = {}
total_calories = 0
for data in valid_text:
    current_food = data.groupdict()
    food[current_food['item']] = {'expiration_date': current_food['date'],
                                       'calories': current_food['calories']}
for key, value in food.items():
    total_calories += int(value['calories'])

days = total_calories // 2000
print(f'You have food to last you for: {days} days!')
for key, value in food.items():
    item = key
    ex_date = value['expiration_date']
    cal = value['calories']
    print(f'Item: {item}, Best before: {ex_date}, Nutrition: {cal}')
