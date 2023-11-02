names = ['li', 'zhang', 'wang', 'chen']

print(f"Opoos, {names[1]} can't come")
names.append('fang')
names.remove('zhang')



print('I just found a big table')
names.insert(0, 'da')
names.insert(2, 'ma')
names.append('liang')
for name in names:
    print(f"{name}, would you like come for dinner")
  
print('My table can\'t be delived in time')
while len(names) > 2:
    name = names.pop()
    print(f"{name}, sorry you can't come")

for name in names:
    print(f"{name}, you can still come for dinner")

del names[0]
del names[0]
print(names)