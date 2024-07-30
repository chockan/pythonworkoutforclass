# Comprehension:
# Dictionary comprehensions can be used to create dictionaries from arbitrary key and
# value expressions:
z={x: x**2 for x in (2,4,6)}
print(z)
# {2: 4, 4: 16, 6: 36}
dict11 = {x: x*x for x in range(6)}
print(dict11)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

a=10
print(a)
del a
print(a)
