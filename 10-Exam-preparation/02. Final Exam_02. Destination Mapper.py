import re
data = input()
pattern = r"(?<=([=/]))[A-Z][a-zA-Z]{2}([a-zA-z]+)?(?=(\1))"

valid_place = re.finditer(pattern, data)
matched_place = [place.group()for place in valid_place]
travel_points = len("".join(matched_place))
places = ", ".join(matched_place)
print(f'Destinations: {places}')
print(f'Travel Points: {travel_points}')
