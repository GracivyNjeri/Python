# Tuples
# create an empty tuple
my_tuple=()

# check its type
print(type(my_tuple))

# when creating a tuple with a single element, put a comma after it
my_tuple=(9)
my_tuple2=(9,)

print(type(my_tuple))
print(type(my_tuple2))

# populate our my_tuple
my_tuple = (1,2,3,4,5)

# tupples supporting indexing
my_tuple[0]
my_tuple[2]
my_tuple[-2]
my_tuple[-1]
print(my_tuple)

# tuples are immutable -> you can't add or modify an element
#my_tuple[1]= 10                                                              

# remove an item
#del my_tuple[1]

# tuple assignment -> tuple parking and unpacking
(vendor,model,ios)= ('cisco',2600,12.3)
print(vendor) #->  cisco
print(model) #->  2600
print(ios) #->  12.3

# if you have different number of the elements, a ValueError will return
tuple2=(1,2,3,4)
(p,x,y,z)=tuple2
print(p)
print(x)
print(y)
print(z)

(a,b,c)=(10,20,30)
print(a)
print(b)
print(c)

# TUPLES - METHODS
# we can use the len() function to find the number of element in a tuple
print(len(my_tuple))

# we have the min() and max() functions available for finding the lowest and greatest value inside a tuple
print(min(tuple2))
print(max(tuple2))

# we can also concatenate and multiply a tuple ,using the same old plus and multiplication operators
# concatenation
print(tuple2 + (5,6,7,8))

# repeating/multipling a tuple
print(tuple2 * 5)

# indexing
print(tuple2[0:2])
print(tuple2[:2])
print(tuple2[1:])
print(tuple2[:])
print(tuple2[-2:])
print(tuple2[::-1])
print(tuple2[::-2])

# membership-> 'in' and 'not in ' keywords
print(3 in tuple2)
print(5 not in tuple2)

# we can use the del() command to delete the entire tuple
del tuple2
print(tuple2)
