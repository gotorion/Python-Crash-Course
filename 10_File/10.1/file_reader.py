with open('test.txt') as file_object:
    contents = file_object.read()
print(contents)

file_name = 'test.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
