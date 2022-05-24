# Welcome to our Python playground!
a = [[1,2,3]]
b = a[:] # shallow

c = a[0] # deep
c.append(4)

print(a, b)