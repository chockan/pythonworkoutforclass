# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.keys())
# print(info.values())
# print(info.items())


# dict1 = {"brand":"mrcet","model":"college","year":2004}

# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# Access items
band = {
    "vocals": "Plant",
    "guitar": "Page"
}



print(band["vocals"])
print(band.get("guitar"))

band["vocals"] = "Coverdale"

print(band)



band.update({"bass": "JPJ"})
print(band)

print(band.pop("bass"))
print(band)


# band.popitem() # tuple
# print(band)

band.clear()
print(band)

# del band

# print(band)






