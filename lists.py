list1= []

#  check the type of variable
print(type(list1))

# check the length of the list
print(len(list1))

list1=['cisco','juniper','avaya',10,10.5,-11]

# check the length
print(len(list1))

print(list1)

# how to access list elements -> indexing
print(list1[0])

# print(list1[100])

# check that lists are indeed mutable
list1[2]='hp'
print(list1[2])

list2=[-11,2,12]
print(list2[2])

# min() -> finds the small element in a list
# max() function finds the largest element in  a list
list2=[-11,2,12]
print(f'the smallest number is:{min(list2)}')
print(f'the largest number is:{max(list2)}')

# what about string?
list3=['a','b','c']
# print('a'>'A')
print(min(list3))
print(max(list3))

# list methods
# append()-> adds a new element to a list
list1.append(100)
print(list1)

# remove an element from a list
# 1.del command
del list1[4]
print(list1)

# 2.pop() -> another way to remove an element by its index
list1.pop(0)
print(list1)

# 3.remove() method-> specify the element you want to remove
list1.remove('hp')
print(list1)

# inserting an element at a partiular index-> insert() method
list1.insert(2,'nortel')
print(list1)

# append a list to another list-> extend()
list4=[9,99,999]
list1.extend(list4)
print(list1)

# index() and count()
print(list1)
print(list1.count(-11))
# append to list1
list1.append(10)
list1.append(10)
list1.append(10)
list1.append(-11)
print(list1)
print(list1.count(-11))
print(list1.count(10))

# find index of an element in a list
print(list1.index('nortel'))

# sorting a list-> in an ascending order-> sort()
list4.append(1)
list4.append(25)
list4.append(500)
print(list4)

list4.sort()

# reverse()-> sorts a list in descending order
list4.reverse()

# sorted()-> sort and create a new list in memory
new_list=sorted(list4, reverse=True)
print(new_list)
print(list4)

# concatenate a list
print(list1 + list4)

# repeating a list
print(list4 * 5)

# list slices\ slicing
list5=[1,2,3,'a','b','c']

# extract the first three characters-> [1,2,3]
print(list5[0:3])

# extract [3,'a','b']
print(list5[2:5])

# extract [1,2,3,'a','b','c']
print(list5[0:])

# using negative indexes, extract[3,'a','b']
print(list5[-4:-1])

# using -ve index, extract['a','b','c']
print(list5[-3:])

# using -ve index[1,2,3]
print(list5[-6:-3])

# use a step to extract[1,3,'b']
print(list5[0:5:2])

# use a step to reverse the list['c','b','a',3,2,1]
print(list5[::-1])