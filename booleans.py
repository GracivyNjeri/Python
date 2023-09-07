# Booleans - True or False values
print(1==1)  # returns True
print(1==2)  # returns False
print('python'== 'Python')  # returns False
print(3<=4)  # returns True -> logical operators          

# Booleans Operations
# 1. and -> means both opperands should be true, in order to have the entire expression evaluated as true

print((1==1) and(1==3))  # returns False

# 2. or ->if at least one of the expression evaluate to True, then the final results is true

a=1 >=3
b=2 !=4
print(a or b)

# 3. not -> NOT operator means simply denying an expression, if that expression is True , then denying it will result to False and vice versa

c=2 > 5
print(not(c)) 