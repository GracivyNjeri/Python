userName=input('Wawey')
print(f'hello{userName}')

# solution 1
# prompt the user fo their name
student_name=input('please enter your name: ')

# create an empty list to store the student info
student_info=[]

# get marks of the 5 units
maths=int(input('enter your marks for maths: '))
english=int(input('enter your marks for english: '))
kiswahili=int(input('enter your marks for kiswahili: '))
science=int(input('enter your marks for science: '))
sst=int(input('enter your marks for sst: '))

# store the marks in the list
#student_info=[student_name,maths,english,science,kiswahili,sst]

student_info.append(student_name)
student_info.append(maths)
student_info.append(english)
student_info.append(science)
student_info.append(kiswahili)
student_info.append(sst)
print(student_info)

# calculate the total score
#total_score=student_info[1] + student_info[2] + student_info[3] + student_info[4] + student_info[5]

student_marks_list=student_info[1: ]

total_score= student_marks_list[0]+student_marks_list[1] + student_marks_list[2] + student_marks_list[3] + student_marks_list[4] 

# calculate the average
#average_mark=total_score / 5
average_mark=sum(student_marks_list)/ len(student_marks_list)

# display the student info
print(f'hello,{student_info[0]}, Average score is: {average_mark}%')

# solution 2
# prompt user for the name
name=input('enter your name: ')
age=int(input('enter your age: '))

# calculate the decade(s) the user has lived
decades_lived=age// 10

# check if the decades is greater than 1-> assign an 's'
s='s' if decades_lived > 1 else''

# convert the age into minutes
age_in_minutes= age * 365.25 * 24 * 60

# display the decades lived by user
print(f'hello,{name}, you have lived for: {decades_lived} decade{s} and {age_in_minutes}minutes.')