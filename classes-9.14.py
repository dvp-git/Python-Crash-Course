# Exerecise 9.14 Dice

from random import randint
x = randint(1,6)

### Making a class Die

class Die():
    """ class called Die"""
    def __init__(self, sides):
        """initializing the attributes of the Die"""
        self.sides = sides

    def roll_die(self):
        """prints a random number"""
        return randint(1,self.sides)


six_sided_die = Die(6)


results =[]
for roll in range(10):
    result = six_sided_die.roll_die()
    results.append(result)
print(results)


Ten_sided_die = Die(10)

results =[]
for roll in range(10):
    result = Ten_sided_die.roll_die()
    results.append(result)
print(results)


