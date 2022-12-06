# print('Welcome')
# variables & datatypes 
'''
name = 'Arbin Koirala'
age = 40
salary = 10000.0
is_married = True

print(name)
print('Name:' + name)
#print('Age:' + age) [python maa chai str raa int concat garnako laagi "," use garnu parxa]
print('Age:' , age)
print(f'Age : {age}, Salary : {salary}') #yesley pani python maa concat garna kaam laagxa
print('Marital status:' , is_married)
'''

#user sangai magna lai 
'''
from os import name
Name = input('Enter your name :')
Salary = input('Enter your salary:')

print(Name)
print(Salary)
print('Mr/Mrs' ,Name,'your salary is :',float(Salary)*0.15)
'''

# Operators
'''
1. Arithmatic : + - * / ** // %
2. Logical : and or not
3. Relational:
4. Assignment: =
5. Concatenation: =
6. Membership: in    not in 
7. Identity: is      is not
'''


'''
a = 10
b = 25
c =10
print ( b/a)
print (a<b or a==b)
print (a<b and a==b)
print (a != b)

# assignment operator

a += 5
print(a)

a %= 4
print(a)
'''


'''
 Conditional Statements
1. if


a = input('Enter the first number')
b = input('Enter the second number')

if a>b:
    print('a is greater than b')
elif a<b:
    print('a is less than b')
print('bye')
'''


'''
print if a user given number is odd or even
a = float(input('Enter the number'))
 
if a % 2 == 0:
    print('No is even')
else:
    print ('No is odd')

'''



'''
Loops in python 
1. for
2. while 
'''

# for(initialize; final_condition; increment/decrement)
# for(a=1; a<=10; a++)
'''
for i in range(1, 6, 1):
    print(i)

for j in range(10, 0, -1):
    print(j)
'''

'''
 print if a given number is prime or composite 

a = int(input('Enter a number'))

for i in range (2, a//2 + 1, 1):
    
    if a%i == 0 :
        print('It is composite')
        break
else:
    print('It is prime')

'''

 
# while 
'''
j=1
while j<=10:
    print(j)
    j +=1


a = int(input('Enter a number'))

j=2
while a//2 + 1:
    if a%j==0:
        print('Composite')
        break
else:
    print('Prime')
'''



'''
# print day according to user given number 

a = int(input('Enter any no you want from 0 to 6'))


if a==0:
    print('Sunday')
elif a==1:
    print('Monday')
elif a==2:
    print('Tuesday')
elif a==3:
    print('Wednesday')
elif a==4:
    print('Thursday')
elif a==5:
    print('Friday')
elif a==6:
    print('Saturday')
else:
    print('Incorrect number please try again')
'''



'''
# Print factorial of user given number 

a = int(input('Enter any number you want:'))
factorial=1
if a == 0:
    print('Enter another number')
elif a > 0 :
    for i in range(a, 0, -1):
        factorial = factorial * i
print(factorial)
'''

'''
# Print factors of a user given number 

a = int(input('Enter a number'))

for i in range(1, a+1, 1):
    if a%i == 0:
        print(i)
'''

'''
# fibonacci series (0 1 1 2 3 5 8 .......)
d = int(input('Any number'))
a = 0
b = 1

print(a)
print(b)

for i in range(d):
    c = a + b
    if c <= 100:
        print(c)
    
        a = b
        b = c
    else:
        break
'''

'''
# nested loop 
# multiplication of a number 

n1 = 10
n2 = 10

for i in range(1, n1+1):
    for j in range(1, n2+1):
        print(i, 'x', j, '=', i*j, end=' ')
    print()
'''



'''
*              1
**             12 
***            123
****           1234
*****          12345
'''
'''
for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()


for i in range(1,6):
    for j in range(i):
        print(i, end=' ')
    print()
'''


# print('I am a good boy\nand the viewer is also good')


#CRUD operation
# C -> Create
# R -> Read
# U -> Update
# D -> Delete



# Calculator 

'''a = int(input('Enter the first number'))
b = int(input('Enter the second number'))

print('Addition:', a+b)
print('Subtraction:', a-b)
print('Multiplication:', a*b)
print('Division:', a/b)
print('Modulo:', a%b)'''


# Calculator **

a = int(input('Enter the first number'))
b = int(input('Enter the second number'))

n = int(input('Enter no 1 to 5 to perform different operation\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Modulo'))

if n==1:
    print('Addition:', a+b)
elif n==2:
    print('Subtraction:', a-b)
elif n==3:
    print('Multiplication:', a*b)
elif n==4:
    print('Division:', a/b)
elif n==5:
    print('Modulo:', a%b)
else:
    print('Invalid no please choose between 1 to 5')
