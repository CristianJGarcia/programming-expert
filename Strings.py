var = "algoexpert".upper().replace("o", "i").capitalize().lower().split("e")

print("foo".join(var))

# Write your code here.

# You'll have to use the following strings:
# 1) "Enter an integer: "
# 2) "What is your name? "
# 3) "Hello, "
number = input("Enter an integer: ")

if number.isdigit():
    name = input("What is your name? ")
    print(f"Hello, {name.upper()}")
else:
    print(number.capitalize())

# Write your code here.

# You'll have to use the following strings:
# 1) "Enter a sentence: "
# 2) "There are _ words in this sentence"
sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"There are {len(words)} words in this sentence")
