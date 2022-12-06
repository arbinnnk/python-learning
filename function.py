# function 
# Parameterized   2. non parameterized

#1. Return type  2.non return type

'''
def add(a, b):
    print(a+b)

n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))
add(n1, n2)'''

# non parameterized

'''
def add_np():
    a = int(input('Enter first number'))
    b = int(input('Enter second number'))
    print(a+b)
add_np()  
'''



#Exception /handling
#prime number or composite
def check_number():
    try:
        n = input('Enter a number')
        # if n.isalpha():
        #     print('Invalid entry')
        #     check_number()

        a = int(n)
        for i in range(2,a//2+1):
             if a%i==0:
                print('Composite')
                break
             else:
                print('Prime')

             check_number()
    except Exception as e:
        print('Invalid number:', e)
        check_number()
    finally:
        check_number()

check_number()



#

















