value = 5
x = "global"


def foo():
  global value
  value = 10

print(value)
foo()
print(value)

value = 20
foo()
print(value)

def foo():
    global x
    print(x, end=",")
    x = "local"
    print(x, end=",")

foo()
print(x, end="")