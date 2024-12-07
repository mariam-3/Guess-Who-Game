#Mariam

import random


name =""
eye_colour = ""
hair_colour = ""
accessory = ""

class Person():
  def __init__ (self, name, eye_colour, hair_colour, accessory):
    self.name = name
    self.eye_colour = eye_colour
    self.hair_colour = hair_colour
    self.accessory = accessory

  
  def secret_character(self, message, eye_colour, hair_colour, accessory, discarded):
    print("The person is", self.message)
    self.discarded = False
  def discard(self, discarded):
    self.discarded = True

character = Person("Jennifer", "blue eyes", "red hair", "glasses")

print('I met a person named', character.name + '. ')
print('She has', character.eye_colour, ",", character.hair_colour, 'and wears', character.accessory)
print('')

people = []

with open('people.txt') as f:
  counter = 0
  for line in f:
    split1 = line.strip().split(',')
    people.append(Person(split1[0], split1[1], split1[2], split1[3]))
    print("Name is:", people[counter].name)
    print("Eye colour is:", people[counter].eye_colour)
    print("Hair colour is:", people[counter].hair_colour)
    print("Accessory is:", people[counter].accessory)
    counter += 1
    print('')

print('''

''')

secret_character = random.choice(people)

while True:
  counter = 0
  question = input('''What would you like to guess? 
  Type 1. to guess the name, 
  Type 2. to guess the eye colour, 
  Type 3. to guess hair colour or 
  4. To guess the accessory.''')

  if question == '2':
    counter += 1
    print('')
    print('Guess the eye colour')
    guessed_eyes = input('>')
    if guessed_eyes.lower() == secret_character.eye_colour.lower():
      print('Yes')
    else:
      print('No')

  elif question == '3':
    counter += 1
    print('')
    print('Guess the hair colour')
    guessed_hair = input('>')
    if guessed_hair.lower() == secret_character.hair_colour.lower():
      print('Yes')
    else:
      print('No')

  elif question == '4':
    counter += 1
    print('')
    print('Guess the accessory')
    guessed_accessory = input('>')
    if guessed_accessory.lower() == secret_character.accessory.lower():
      print('Yes')
    else:
      print('No')

  elif question == '1':
    counter += 1
    print('')
    print('Guess the character')
    guessed_name = input('>')
    if  guessed_name.lower() == secret_character.name.lower():
      print('You guessed it!')
      print('Your score is', counter)
      break
    else:
      print('Nope! Try again!') 

  else: 
    print('')
    print("sorry, that's not an option")