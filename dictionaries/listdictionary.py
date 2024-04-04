# List of Dictionaries:
customers = [{"uid":1,"name":"John"},{"uid":2,"name":"Smith"},{"uid":3,"name":"Andersson"},]
print(customers)
# [{'uid': 1, 'name': 'John'}, {'uid': 2, 'name': 'Smith'}, {'uid': 3, 'name': 'Andersson'}]
# ## Print the uid and name of each customer
for x in customers:
    print(x["uid"], x["name"])

# ## Modify an entry, This will change the name of customer 2 from Smith to Charlie
customers[2]["name"]="charlie"
print(customers)
# [{'uid': 1, 'name': 'John'}, {'uid': 2, 'name': 'Smith'}, {'uid': 3, 'name': 'charlie'}]
# ## Add a new field to each entry
for x in customers:
    x["password"]="123456" # any initial value
print(customers)

# [{'uid': 1, 'name': 'John', 'password': '123456'}, {'uid': 2, 'name': 'Smith', 'password':
# '123456'}, {'uid': 3, 'name': 'charlie', 'password': '123456'}]
# ## Delete a field
del customers[1]
print(customers)
# [{'uid': 1, 'name': 'John', 'password': '123456'}, {'uid': 3, 'name': 'charlie', 'password':
# '123456'}]
del customers[1]
print(customers)
# [{'uid': 1, 'name': 'John', 'password': '123456'}]
# ## Delete all fields
for x in customers:
    del x["uid"]
print(x)
# {'name': 'John', 'password': '123456'}
