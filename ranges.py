# ranges
# http://codeskulptor.org -> py2

# create a range of 10
r=range(10)

# check type
print(type(r))

# print the range
print(list(r))

r=list(range(1,11))
print(r)

# indexing
print(range(10)[1])
print(range(1,9)[1])

# 0,2,4,6,8
print(list(range(10)[::2]))

# -2,-4,-6,-8
print(list(range(-2,-10,-2)))

# -8,-6,-4,-2
print(list(range(-2,-10,-2)[::-1]))