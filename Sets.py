# Write your code here.

# You'll have to use the strings:
# "Enter a character: "
# "Number of unique characters entered: _"

chars = set()

while True:
    character = input("Enter a character: ")

    if character in chars or len(character) > 1:
        print(f"Number of unique characters entered: {len(chars)}")
        break

    chars.add(character)

def compare_lists(lst1=[], lst2=[]):
    # Write your code here.
    x = set(lst1)
    y = set(lst2)
    result = x.intersection(y)

    return len(result)

print(compare_lists([1, 2, 3], [1, 1, 1]))











