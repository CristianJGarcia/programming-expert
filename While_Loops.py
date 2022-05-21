# Write your code here.

# You'll have to use the following strings:
# 1) "Enter a number: "
# 2) "You entered _ numbers."

numbers = 0
num = 0

while num != 5:
    num = int(input("Enter a number: "))
    numbers += 1

print(f"You entered {numbers} numbers.")

# Write your code here.

# You'll have to use the following strings:
# 1) "Enter a word: "
# 2) "The average word length is: _."

average = 0
words = 0
string = ""

while True:
    string = input("Enter a word: ")
    if string == 'q' or string == "quit":
        break
    average += len(string)
    words += 1

if words > 0:
    average = average / words
    print(f"The average word length is: {average}.")

# Write your code here.

numbers = [1,3,6,10,15,21]

index = 0

while index < len(numbers):
    print(numbers[index] * numbers[index])
    index += 1