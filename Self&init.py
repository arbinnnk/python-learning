# Self & init Constructor 
'''
class Employee:
    no_of_leaves = 8

    def printdetails(self):
        return f"The name is :{self.name}. email is :{self.email} and salary is :{self.salary}"


   
Arbin = Employee()
Abiral = Employee()

Arbin.name = "Arbinnn"
Arbin.email = "arbin47.koirala@gmail.com"
Arbin.salary = "45K"

Abiral.name = "Abiralblon"
Abiral.email = "blon.abiral@gmail.com"
Abiral.salary = "50k"

print(Abiral.printdetails())
'''


class Employee:
    no_of_leaves = 8

    def __init__(self, name1, email1, salary1):
        self.name = name1
        self.email = email1
        self.salary = salary1
        

    def printdetails(self):
        return f"The name is :{self.name}. email is :{self.email} and salary is :{self.salary}"


   
Arbin = Employee('Arbinnn','arbin47.koirala@gmail.com',45)
Abiral = Employee('Abiralblon','blon.abiral@gmail.com',50)

# Arbin.name = "Arbinnn"
# Arbin.email = "arbin47.koirala@gmail.com"
# Arbin.salary = "45K"

# Abiral.name = "Abiralblon"
# Abiral.email = "blon.abiral@gmail.com"
# Abiral.salary = "50k"

# print(Abiral.printdetails())

print(Arbin.__dict__)