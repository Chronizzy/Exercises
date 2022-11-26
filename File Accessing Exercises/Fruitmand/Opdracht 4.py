from fruitmand1 import fruitmand
import random

ASK = int(input('hoeveel? '))
fruits = []

for i in fruitmand:
    fruits.append(i['name'])
    
randomFruit = random.choice(fruits)

for j in range(ASK):
    print(randomFruit)