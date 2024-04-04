# To access specific value of a dictionary, we must pass its key,
dict1 = {"brand":"mrcet","model":"college","year":2004}
x=dict1["brand"]
print()
# 'mrcet'
# To access keys and values and items of dictionary:
dict1 = {"brand":"mrcet","model":"college","year":2004}
print(dict1.keys())
# dict_keys(['brand', 'model', 'year'])
print(dict1.values())
# dict_values(['mrcet', 'college', 2004])
print(dict1.items())
#dict_items([('brand', 'mrcet'), ('model', 'college'), ('year', 2004)])
for items in dict1.values():
    print(items)
# mrcet
# college
# 2004
for items in dict1.keys():
    print(items)
# brand
# model
# year
for i in dict1.items():
    print(i)
# ('brand', 'mrcet')
# ('model', 'college')
# ('year', 2004)
# Some more operations like:
# • Add/change
# • Remove
# • Length
# • Delete
# Add/change values: You can change the value of a specific item by referring to its key
# name
dict1 = {"brand":"mrcet","model":"college","year":2004}
dict1["year"]=2005
print(dict1)
# >>> dict1
# {'brand': 'mrcet', 'model': 'college', 'year': 2005}
# Remove(): It removes or pop the specific item of dictionary.
dict1 = {"brand":"mrcet","model":"college","year":2004}
print(dict1.pop("model"))
# college
# >>> dict1
# {'brand': 'mrcet', 'year': 2005}
# Delete: Deletes a particular item.
x = {1:1, 2:4, 3:9, 4:16, 5:25}
del x[5]
print(x)
# Length: we use len() method to get the length of dictionary.
# >>>{1: 1, 2: 4, 3: 9, 4: 16}
x={1: 1, 2: 4, 3: 9, 4: 16}
y=len(x)
# >>> y
# 4
# Iterating over (key, value) pairs:
x = {1:1, 2:4, 3:9, 4:16, 5:25}
for key in x:
    print(key, x[key])
# 1 1
# 2 4
# 3 9
# 101
# 4 16
# 5 25
for k,v in x.items():
    print(k,v)
# 1 1
# 2 4
# 3 9
# 4 16
# 5 25