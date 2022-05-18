# Write your code here.

# You'll have to use the following strings:
# 1) "Enter a string: "
# 2) "Enter a number: "
strings = []
numbers = []

for i in range(5):
    strings.append(input("Enter a string: "))

num = 0

for j in range(3):
    num = int(input("Enter a number: "))
    if  0 <= num <= 4:
        numbers.append(num)

for num in numbers:
    print(strings[num], end="")