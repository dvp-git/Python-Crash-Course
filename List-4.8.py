# Exercise 4.8 Cubes

#creating an empty list of cubes
cubes = []

#generating the sequence using logic
for digit in range(1,11):
    cube = digit**3
    cubes.append(cube)

#Printing each value in cubes
for cube in cubes:
    print(cube)

