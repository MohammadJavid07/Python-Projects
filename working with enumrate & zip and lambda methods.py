developers = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
# Using enumerate to get index and value
for index, developer in enumerate(developers):
    print(f"{index} : {developer}")

# Using start parameter in enumerate
for index, developer in enumerate(developers, 1):
    print(f"{index} : {developer}")

#Using zip to combine two lists
provinces = ['Ontario', 'Quebec', 'British Columbia', 'Alberta', 'Manitoba', 'Saskatchewan', 'Nova Scotia', 'New Brunswick', 'Newfoundland and Labrador', 'Prince Edward Island']
for developer, province in zip(developers, provinces):
    print(f"{developer} : lives in {province}")

# Using lambda to find the length of each developer's name
name_lengths = list(map(lambda x: len(x), developers))
print("Name lengths:", name_lengths)
