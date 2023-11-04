for value in range(1, 5): #左闭右开
    print(value)
  
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
      squares.append(value ** 2)
print(squares)

digits = list(range(0, 10))
print(min(digits))
print(max(digits))
print(sum(digits))