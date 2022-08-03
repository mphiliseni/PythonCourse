# Boolean expression (True or False)
from curses import nl
from pickle import FALSE


bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool))

bool5 = "True" #Boolean String
print(type(bool5))

nl() #New line

#Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 5
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #true
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True