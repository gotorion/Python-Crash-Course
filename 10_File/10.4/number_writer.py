import json

numbers = [2, 3, 4, 5, 6, 11]
file_name = 'numbers.json'
with open(file_name, 'w') as f:
    json.dump(numbers, f)

json_number = []
with open(file_name) as f:
    json_number = json.load(f)
print(json_number)
