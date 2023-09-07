# create an empty dictonary
dict1={}

# check the type of dict1
print(type(dict1))

# add some data to dict1
dict1={'Vendor':'Cisco','Model':'2600','IOS':'12.4','Ports':'4'}

# DICTIONARIES - METHODS
# extract the corresponding value of a specified key
# output -> 2600
print(dict1['Model'])

# add a new key value pair to the dictonary
dict1['RAM']='128'

# modify the value of a specified key -> 12.4 to 15.6
dict1['IOS']='15.6'

# we can also delete a pair from the dictonary using the del command
del dict1['Ports']

# find the number of key-value pair
print(len(dict1))

# we can also verify if a certain value string is a key in a dictonary using 'in or 'not in'
print('Ports'in dict1)
print('IoS' in dict1)

# print the data
print(dict1)

# three important python mehods to deal with dictonaries
# 1.keys() method
print(list(dict1.keys()))

# 2.values() returns a list that contains values of the dictonary as elements
print(list(dict1.values()))

# 3.items() returns a list of tuples,each tuple containing a key and a value of each dict pair
print(list(dict1.items()))

from pprint import pprint

# question
dict2=dict(a=list(range(1,11)),b=list(range(11,21)),c=list(range(21,31)))
pprint(dict2)

dict3={'a':list(range(1,11)),'b':list(range(11,21)),'c':list(range(21,31))}
pprint(dict3)

a=list(range(1,11))
b=list(range(11,21))
c=list(range(21,31))

pprint({'a':a,'b':b,'c':c})

# output-> 13
print(dict3['b'][2])
