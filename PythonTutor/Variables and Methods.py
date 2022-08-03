# Variable mean something and Var can change 
from email.quoprimime import quote

quote = "All is fair in love and war."
print (quote)

# Methonds are functions  available for giving object

# Uppercase
print (quote.upper())

# LowerCase
print(quote.lower())

# Title Case
print(quote.title())

# Count the characters
print(len(quote))


name = "Mphiliseni"# String
age=28 #int
gpa= 2.8 #float - has a decimal

print (int(age))
print(int(20.1))
print(int(30.9)) #will round? No.

print ("My name is " + name + " and I am " + str(age) + " years  old.") 

age += 1
print(age)


birthday = 1
age += birthday
print(age)