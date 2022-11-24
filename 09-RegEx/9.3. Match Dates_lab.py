import re

dates = input()
pattern = r"(?P<Day>\d{2})(?P<separator>[\./-])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"

matched_dates = re.finditer(pattern, dates)

for date in matched_dates:
    current_date = date.groupdict()
    print(f'Day: {current_date["Day"]}, Month: {current_date["Month"]}, Year: {current_date["Year"]}')


# втори вариант
# import re
#
# dates = input()
# pattern = r"(?P<Day>\d{2})(?P<separator>[\./-])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"
#
# matched_dates = re.findall(pattern, dates)
# for date in matched_dates:
#     print(f'Day: {date[0]}, Month: {date[2]}, Year: {date[3]}')
