info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())

for key, value in info.items():
  a=10
  b=50
  print(key)
  print(value)
  print(f"The value corresponding to the key {key} is {value}") 
  print(f"The value corresponding to the key {a} is {b}") 
  