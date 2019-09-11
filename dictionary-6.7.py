## Exercise 6.7 People

## Make an empty list called people

people = []

## Making 2 dictionaries representing 2 different people

person = {'first' : 'Darryl',
            'last': 'Prabhu',
            'Code':'dprabhu',
            }
people.append(person)

person = {'first' : 'Rahul',
            'last': 'Luhar',
            'Code':'raHul',
            }
people.append(person)


person = {'first' : 'Adithya',
            'last': 'Hegde',
            'Code':'hegde5',
            }
people.append(person)


## people is a list

for person in people[0:3]:
                     print("\nFirst Namw is : " + person['first'])
                     print("Last Namw is : " + person['last'])
                     print("Code Namw is : " + person['Code'])
