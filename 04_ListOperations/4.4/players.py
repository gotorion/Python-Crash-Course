players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:2])
print(players[3:])
print(players[:])
# 遍历切片
for name in players[1:4]:
    print(f"{name}, hi there")