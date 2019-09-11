## Exercise 4.11 My Pizzas, Your Pizzas

favourite_pizza = ['pepporoni','chicken','sausage']

for pizza in favourite_pizza:
    print("I like " + pizza + " the best")

print("Pizza has always been one of my favourite dishes")

#Copy of the pizza
friend_pizzas = favourite_pizza[:]

favourite_pizza.append('BBQ')

friend_pizzas.append('corn')

## My favourite pizza
print("My favourite pizzas are:")
for pizza in favourite_pizza:
    print(pizza)

##Friend's favouorite pizza
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

