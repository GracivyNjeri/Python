
string1='cisco router'
# find length
# print(len(string1))
# print(string1[12])

# String Operations and Method (Python Strings)
# Find the index of a charater inside a given string -> index() method

a='Cisco Switch'
print(a.index("i"))

print(a.index(" "))

# find how many times a character appears in a string\ sequence
print(a.count("C"))

# find() method -> returns the index where the character begins
print(a.find('sco'))   #returns index 2
print(a.find('xyz'))   # returns index -1

# lower() and upper() methods
print(a.lower())  #return the string in lower case
print(a.upper())  #return the string in upper case 

# startswith() and endswith() methods
print(a.startswith('C'))  #returns true
print(a.endswith('H'))    # returns false

b='   Cisco Switch    '

# strip()
print(b)
print(b.strip())

b='$$$Cisco Switch$$$'
print(b)
print(b.strip('$'))

# replace() method
b='   Cisco Switch    '
print(b)
print(b.replace(' ',''))
print(b.replace('i','a'))

# split()
# a string of networking equipment manufactures
c='Cisco,Juniper,Hp,Avaya,Nortel,Huwaei'
print(c.split(','))

# join()
print('_'.join(a))
d='$'.join(b)
print(d)

# String Formatting
first_name='Mitchel'
last_name='Makena'

# concatenation concat()
# 1.using + operator
print(first_name +' ' + last_name)
print('My name is '+ first_name+ ' ' + last_name + '.')

# 2.using format() 
print('My name is {} {}.'.format(first_name,last_name))
print('My name is {first} {last}.'.format(first=first_name,last=last_name))

# 3.using f-string
age=20
print(f'My name is {first_name} {last_name} and I am {age} years old.')

# String Slicing
string1='O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2'

# Slice 10.110.8.9
print(string1[5:15])

# slicing without the second index
print(string1[5:]) 

# slicing without the first index
print(string1[:10])

# slicing without any index
print(string1[:])

# Negative Indexes
print(string1[-5])

# 'Ethernet' substring
print(string1[-9:-1])

# extract the last five characters -> rnet2
print(string1[-5:]) 

# extract the beginning of the string and exclude the last 5 characters
print(string1[:-5])

# Slicing using a step
# syntax for a step
# string_name [start: stop: step]
print(len(string1))
print(string1[::2])
print(string1[0:60:2])

# reverse a string using a step
print(string1[::-1])