string1 = "aabbcsdw"
string2 = "abbbcsdd"

# Write your code here.
for index, letter in enumerate(string1):
    if letter == string2[index]:
        print(letter)

lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

# Write your code here.
for i in range(1, len(lst), 2):
    if lst[i] % 2 == 0:
        print(lst[i])

lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

# Write your code here.
for arr in lst:
    sum = 0
    for i in arr:
        sum += i
    print(sum)

lst = [-2, 0, 4, 5, 1, 2]

# Write your code here.
for i in range(len(lst)):
    if len(lst) == (i + 1):
        break
    print(lst[i] + lst[i + 1])