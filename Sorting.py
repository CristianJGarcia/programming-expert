people = {"Tim": 21, "Joe": 18, "Sarah": 25, "Jennie": 26, "Bill": 34}

result = sorted(people, key=people.get) # returns a new list
print(result)