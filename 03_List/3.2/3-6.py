names = ['li', 'zhang', 'wang', 'chen']
for name in names:
    print(f"{name}, would you like come for dinner")

print(f"Opoos, {names[1]} can't come")
names.append('fang')
names.remove('zhang')



print('I just found a big table')
names.insert(0, 'da')
names.insert(2, 'ma')
names.append('liang')
for name in names:
    print(f"{name}, would you like come for dinner")