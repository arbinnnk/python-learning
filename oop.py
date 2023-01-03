'''
OOP
-----
Class & Objects

Features of OOP
1. Encapsulation
2. Inheritance
3. Polymorphism
    a. Method overloading
    b. Method overriding
4. Abstraction (Interface)
'''

'''
online News portal
    User
        name, mobile, email, username, password
        register(), update(), view(), login(), delete()
    News
        topic, date, details, author, category
        add() view() update() view()
    Comment
        fullname, email, comments, status(approved/requested)
        add() view() delete()

Online Student Enrollment
    User
        name, mobile, email, username, password, type
        register(), update(), view(), login(), delete()
    course
        title duration  fee shift affiliation department status
        add(), view() update() delete()
    Enrollment
        user course date



online Job Portal
    User
        name, mobile, email, username, password, image, cv, type
        register(), update(), view(), login(), delete()
    Job
        title detail requirement salary company vacancy_no category
        add(), update(), view(), delete()
    Application



Online shopping (E-commerce)
    User
        name, mobile, 
    Product
        name price details stock features category brand types
'''
'''
class User:
    full_name = ''
    mobile = ''
    email = ''
    address = ''
    password = ''
    type = ''

    def register():
        pass

    def view():
        pass

    def login():
        pass

    def search():
        pass

    def update():
        pass

    def delete():
        pass
    '''



# Class -> Template
# Object -> Instances

# Instance Variables
'''
class Students:
    pass

Arbin = Students()
Abiral = Students()
Pratik = Students()
Thaneshwor = Students()

Arbin.Name = 'Arbinnn'
Arbin.Std = 'Bachelor'
Arbin.Roll = 9
Arbin.faculty = 'Bsc.Csit'
Abiral.Name = 'Abiral Blon'
Abiral.Std = 'Bachelor'
Abiral.Roll ='05'
Abiral.faculty = 'Bsc.Csit'

print(Arbin.Name, Abiral.Name)
'''



'''
class Employee:
    no_of_leaves = 8
    
Arbin = Employee()
Abiral = Employee()

Arbin.name = "Arbinnn"
Arbin.email = "arbin47.koirala@gmail.com"
Arbin.salary = "45K"
Abiral.name = "Abiralblon"
Abiral.email = "blon.abiral@gmail.com"
Abiral.salary = "50k"

print(Abiral.no_of_leaves, Abiral.name, Abiral.email, Abiral.salary)
Employee.no_of_leaves = 9
print(Employee.no_of_leaves)
'''


# public
'''
class Animal:
    color = ''
    height = ''
    weight = ''

    def move(self):
        print('It moves')

Bagh = Animal()
Bagh.color = 'white'
Bagh.height = 5.9
Bagh.weight = 68
print(Bagh.color, Bagh.height, Bagh.weight)
'''
# Private
# double underscore -> private, single -> Protected
'''
class Animal:
    __color = ''
    __height = ''
    __weight = ''

    def __init__(self, color_value, height_value, weight_value):
        self.__color = color_value
        self.__height = height_value
        self.__weight = weight_value

    #  setters & getters
    def setColor(self, value):
        self.__color = value

    def getColor(self):
        return self.__color

    def move(self):
        print('It moves')

Bagh = Animal()
Bagh.__color = 'white'
# Bagh.color = 'white'
# Bagh.height = 5.9
# Bagh.weight = 68
# print(Bagh.color, Bagh.height, Bagh.weight)
print(Bagh.__color)


class Dog(Animal):
    def __init__(self, color_value, height_value, weight_value):
        self food = food
        super().__init__(color_value, height_value, weight_value)



class Crocodile(Animal):
    pass

class Bird(Animal):
    pass
'''
# inheritance
# abstract class