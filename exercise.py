questions = ['What is area of Nepal?',
        'What is the height of mount everest?',
        'Who is first prime minister of Nepal?',
        'Population of Nepal is:',
        'First Nepali movie is:']

options = [
    ('147181 sq km', '181481 sq km', '174818 sq km', '247181 sq km'),
    ('7747 m', '7789 m', '8848 m', '4484 m'),
    ('BP Koirala', 'Arbin Koirala', 'Bagh Koirala', 'Bhimsen Thapa'),
    ('30000000', '10000000', '174818', '247181'),
    ('Deuta', 'Aama', 'Abc', 'Xyz')
]
score = 0
answers = ['a', 'c', 'd', 'a', 'b']

def show(n):
    print(questions[n])
    print('a.', options[n][0])
    print('b.', options[n][1])
    print('c.', options[n][2])
    print('d.', options[n][3])
    choice = input('Enter a/b/c/d:')
    global score 
    # if choice != 'a' or choice != 'b' or choice != 'c' or choice != 'd':
    if choice not in ['a', 'b', 'c', 'd']:
        print('Invalid selection')
        choice = input('Enter a/b/c/d:')
    if choice == answers[n]:
        score += 1

for i in range(len(questions)):
    show(i)


print("Score is",score)

'''
class ABC:
    var1 = ''
    var2 = '''''