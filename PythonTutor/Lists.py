# List are data Structure| Have brackets []

movies = ["Hacker","Get out", "How High", "Lion King"]
print(movies[1]) #return the second item in the list
print(movies[0]) #return the first item in the list
print(movies[1:3]) #return the first index number given right until the last number, but not include the last number
print(movies[1:])
print(movies[:1])
print(movies[-1]) #return the last item in the list

print(len(movies)) #return the number of items in the list
movies.append("Anaconda")
print(movies) #append to the end of the list

movies.insert(2,"Hustle")
print(movies)

movies.pop() #remove the last item
print(movies)


movies.pop(0) #remove the first item
print(movies)

#combine Movies 

amber_movies = ['Just Go With It', '50 first Dates']
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

grades = [["Mphiliseni", 82], ["Alice", 90], ["Jeff", 73]]
Mphiliseni_grade = grades[0][1]
print(Mphiliseni_grade)

grades[0][1] = 84
print(grades)