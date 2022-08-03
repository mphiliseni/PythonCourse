# functions organize blog of code 
def who_am_i(): #this is a function without parameters
    name = "Mphiliseni" #local variable
    age = 28
    print("My name is " + name + " and I am " + str(age) + " years  old.")
who_am_i()

def add_one_hundres(num):
    print(num + 100)
add_one_hundres(100)

def add(x, y):
    print(x + y)
add(7,7)

def subract(x, y):
    print(x - y)
subract(10,3)

def Minus(x,y):
    print(x - y)
Minus(20,10)

def multiply(x,y):
    return x *y
multiply(7,7)
print(multiply(7,7))


def square_root(x):
    print(x ** .5)
square_root(64)


# new line
def nl():
    print('\n')
nl()