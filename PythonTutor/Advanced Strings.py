
from email.quoprimime import quote
from re import A


My_name = "Mphiliseni"
print(My_name[0]) #First letter
print(My_name[-1]) #Last letter

sentence = "My name is Mphiliseni am software developer"
print(sentence[:4])
print(sentence.split()) #default is a space 

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)

quote = "He said, \"give me all your money\""
print(quote)

too_much_space =  "                Hello                 "
print(too_much_space.strip())

print("A" in "Apple") #true
print("a" in "Apple") #False
letter = "A"
word = "Apple"
print (letter.lower() in word.lower () ) #improved
movies = "The Hangover"
print("My favorite movie is {}.". format(movies))
print("My favorite movie is %s." % movies)
print(f"My favorite movie is {movies}.")