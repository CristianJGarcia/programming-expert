# Write your code here.

# You'll have to use the following strings:
# 1) "Enter a number: "
# 2) "Enter another number: "
# 3) "The sum of these two numbers is:"
# 4) "That is a large sum!"

number = int(input("Enter a number: "))

if 10 <= number <= 20:
    number2 = int(input("Enter another number: "))
    sum = number + number2
    print(f"The sum of these two numbers is: {float(sum)}")
    if sum > 100:
        print("That is a large sum!")


