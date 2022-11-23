countries = [country for country in input().split(", ")]
capitals = [capital for capital in input().split(", ")]
dictionary = dict(zip(countries, capitals))
for countries, capitals in dictionary.items():
    print(f"{countries} -> {capitals}")

