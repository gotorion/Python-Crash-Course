person = {'first_name': 'john',
          'last_name': 'li',
          'age': 20,
          'city': 'wuhan'}

print(person.get('first_name'))
print(person['last_name'])
print(person.get('age'))
print(person.get('city'))
salary_value = person.get('salary', 'This guy has no salary')
print(salary_value)
