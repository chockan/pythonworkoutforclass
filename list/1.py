

#example 1
list1=[1,2,3,'A','B',7,8,[10,11]]
print(list1)

#[1, 2, 3, 'A', 'B', 7, 8, [10, 11]]

#2
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[1:])
print(list1[:1])
#[1]
print(list1[2:5])
#[3, 4, 5]
print(list1[:6])
#[1, 2, 3, 4, 5, 6]
print(list1[1:2:4])
#[2]
print(list1[1:8:2])
#[2, 4, 6, 8]


#list methods
# Delete: Delete a list or an item from a list
x=[5,3,8,6]
del(x[1]) #deletes the index position 1 in a list
print(x)
# [5, 8, 6]
del(x)
print(x) # complete list gets deleted
# Append: Append an item to a list
x=[1,5,8,4]
x.append(10)
print(x)
# [1, 5, 8, 4, 10]
#Extend: Append a sequence to a list.
x=[1,2,3,4]
y=[3,6,9,1]
x.extend(y)
print(x)
# [1, 2, 3, 4, 3, 6, 9, 1]
# Insert: To add an item at the specified index, use the insert () method:
x=[1,2,4,6,7]
x.insert(2,10) #insert(index no, item to be inserted)
print(x)
# [1, 2, 10, 4, 6, 7]
x.insert(4,['a',11])
print(x)
# [1, 2, 10, 4, ['a', 11], 6, 7]
# Pop: The pop() method removes the specified index, (or the last item if index is not
# specified) or simply pops the last item of list and returns the item.
x=[1, 2, 10, 4, 6, 7]
print(x.pop())
# 7
# >>> x
x=[1, 2, 10, 4, 6]
x=[1, 2, 10, 4, 6]
print(x.pop(2))
# 10
# >>> x
# [1, 2, 4, 6]
# Remove: The remove() method removes the specified item from a given list.
x=[1,33,2,10,4,6]
print(x.remove(33))

# [1, 2, 10, 4, 6]
print(x.remove(4))
# >>> x
# [1, 2, 10, 6]
# Reverse: Reverse the order of a given list.
x=[1,2,3,4,5,6,7]
print(x.reverse())
# >>> x
# [7, 6, 5, 4, 3, 2, 1]
# Sort: Sorts the elements in ascending order
x=[7, 6, 5, 4, 3, 2, 1]
print(x.sort())
# >>> x
# [1, 2, 3, 4, 5, 6, 7]
x=[10,1,5,3,8,7]
print(x.sort())
# >>> x
# [1, 3, 5, 7, 8, 10]
