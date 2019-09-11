invites = ['brothers','sisters','parents']
print("Dear" + invites[0] + ",I invite you to my dinner party")
print("Dear " + invites[1] + ",I invite you to my dinner party")
print("Dear " + invites[2] + ",I invite you to my dinner party")

#Parents arent attending
print("unfortunately, " + invites[2]+ " aren't attending")


#Replacing parents with grandparents
invites.remove('parents')
invites.append('grandparents')
print("Dear" + invites[0] + ",I invite you to my dinner party")
print("Dear " + invites[1] + ",I invite you to my dinner party")
print("Dear " + invites[2] + ",I invite you to my dinner party")

#More people = insertinng elements to list
print("More guests are attending")

invites.insert(0,"Neigbours")
invites.insert((len(invites)//2),"children")
invites.append("Friends")

print("Dear" + invites[0] + ",I invite you to my dinner party")
print("Dear " + invites[1] + ",I invite you to my dinner party")
print("Dear " + invites[2] + ",I invite you to my dinner party")
print("Dear" + invites[3] + ",I invite you to my dinner party")
print("Dear " + invites[4] + ",I invite you to my dinner party")
print("Dear " + invites[5] + ",I invite you to my dinner party")

#no new table

print("Can invite only 2 people")
popped_name = invites.pop(5)
print("SORRY " + popped_name + " ,the dinner is cancelled")

popped_name = invites.pop(4)
print("SORRY " + popped_name + " ,the dinner is cancelled")

popped_name = invites.pop(3)
print("SORRY " + popped_name + " ,the dinner is cancelled")

popped_name = invites.pop(2)
print("SORRY " + popped_name + " ,the dinner is cancelled")


print("Dear" + invites[0] + ",I invite you to my dinner party")
print("Dear " + invites[1] + ",I invite you to my dinner party")


del invites[0]
del invites[0]

print(invites)

