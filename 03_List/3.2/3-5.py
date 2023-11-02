names = ['li', 'zhang', 'wang', 'chen']
for name in names:
    print(f"{name}, would you like come for dinner")

print(f"Opoos, {names[1]} can't come")
names.append('fang')
names.remove('zhang')

for name in names:
    print(f"{name}, would you like come for dinner")