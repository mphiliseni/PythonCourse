#Dictionary - key/ value pairs {}

drinks = {"Mango": 1, "CocaCola": 2, "Sprite":3, "Amarura":5} #drink is the key, price is the value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy jr.", "Mort"]}
print(employees)

employees["Legal"] = ["Mphiliseni"] #adds new key:value
print(employees) 

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair
print(employees)

drinks['CocaCola'] = 4
print(drinks) 

print(drinks.get("CocaCola"))