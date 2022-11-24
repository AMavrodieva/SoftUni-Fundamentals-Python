import re

phone_numbers = input()
pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})\b"

matched_phone = re.finditer(pattern, phone_numbers)
valid_number = [phone.group() for phone in matched_phone]
print(*valid_number, sep=", ")

