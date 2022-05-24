# Welcome to our Python playground!

digits = [i for i in range(10)]
print(digits)

even_numbers = [i for i in range(20) if i % 2 == 0]
print(even_numbers)

divisible_by_3 = {i: i % 3 == 0 for i in range(30)}
print(divisible_by_3)

x, y = 13, "hello"
print(f"x = {x}, y = {y}")

x = y = 10
print(x, y)