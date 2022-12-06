'''
Collection in Python
1. Tuple : static, indexed, ordered, allows duplicate member
2. List  : Dynamic, ordered, indexed, allows duplicate member 
3. Set : element can not be changed but new elementscan be added, unindexed, unordered, doesnot allows duplicate member 
4. Range
5. Dictionary
'''

'''
#list
students = ['ram', 'shyam', 'hari', 'sita', 'gita']
student = ['ram', 'bsc csit', '5', 'Kathmandu']
print(students)
students[2]='Tiger'
print(students)

# append ley chai list maa thapdinxa naya element

students.append('Arbin')
print(students)
'''
'''
#Tuple

students_tuple = ('ram', 'shyam', 'Tiger', 'Panther', 'Leopard')
students_set = {'ram', 'shyam', 'Tiger', 'Panther', 'Leopard'}
students_dict = {1:'Tiger', 2:'shyam', 3:'hari', 4:'sita'}

user_info_dict = {'name': 'Tiger Koirala', 'age': 21, 'salary': 'flesh', 'is_married': False}
print(user_info_dict)

for i in user_info_dict:
    print (i, ':', user_info_dict[i])

'''


'''
print(students_tuple)
#students_tuple[2]='john'
print(students_tuple)
print(students_set)
'''

'''
# multidimensional collection
a = [[], [], []]
b = [(), (), ()]
c = ((), (),())

'''

# students  = [
#     {'name':'Arbin', 'age':'21', 'email':'bagh.koirala@gmail.com', 'phoneno':'9849645262'},
#     {'name':'Abiral', 'age':'23', 'email':'abiral.blon@gmail.com', 'phoneno':'9848657573'},
#     {'name':'Thaneshwor', 'age':'23', 'email':'thaneshwor.gurtal@gmail.com', 'phoneno':'9834567821'}]

# print(students[2])

'''
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

n = int(input('Enter a number'))
if n>0 and n<7:
    print(days[n-1])
else:
    print('Invalid')
'''

n = int(input('Enter any to see next value'))
print(n+1)