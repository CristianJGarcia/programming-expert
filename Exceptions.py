# Write your code here.

# You'll have to use the following strings:
# 1) "Enter the numerator: "
# 2) "Enter the denominator: "
# 3) "The numerator is not a number."
# 4) "The denominator is not a number."
# 5) "You cannot divide by 0."
# 6) "This division cannot be performed."
# 7) "The result of this division is _."
# 8) "Goodbye!"

try:

    num = input("Enter the numerator: ")
    den = input("Enter the denominator: ")

    try:
        num = float(num)
    except ValueError as e:
        print("The numerator is not a number.")

    try:
        den = float(den)
    except ValueError as e:
        print("The denominator is not a number.")

    try:
        result = num / den
    except ZeroDivisionError as e:
        print("You cannot divide by 0.")

    print(f"The result of this division is {result}.")

except Exception as e:
    print("This division cannot be performed.")
finally:
    print("Goodbye!")