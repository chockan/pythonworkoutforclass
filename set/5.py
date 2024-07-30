
# nums = {1, True, 2, False, 3, 4, 0}
# nums.add(8)
# print(nums)


# nums = {1,  2, False, 3, 4,}
# morenums = {5, 6, 7}
# nums.update(morenums)

# print(nums)


# one = {1, 2, 3}
# two = {3,2,6, 7}
# print(one.union(two))
# mynewset = one.union(two)
# print(mynewset)

# one = {1, 2, 3}
# two = {2, 3, 4}

# one.intersection_update(two)
# print(one)

# one = {1, 2, 3}
# two = {2, 3, 4}

# one.symmetric_difference_update(two)
# print(one)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo","jj"}
# print(cities.issuperset(cities2))


# # cities3 = {"Seoul", "Madrid","Kabul"}
# # print(cities.issuperset(cities3))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.intersection(cities2))
# print(cities)

# cities3 = cities.intersection(cities2)
# print(cities3)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)
cities.remove("Tokyo")
print(cities)

# cities.clear()
# print(cities)


a=cities.copy()
print(a)




























