
a = 42
b = "42"
c = 42.42
d = "42.42"

print(int(b) + 1) # str(integer) to int
print(int(c) + 1) # float to int
# print(int(d)) # str(float) will not work so
print(float(d) + 1) # str(float) to float
print(str(c)) # float to str
print(str(a)) # int to str