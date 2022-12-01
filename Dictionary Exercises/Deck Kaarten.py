import random


deck = [] 
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
kaarten = ['aas', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer']


while len(deck) < 54:
    if deck.count('joker') < 2:
        deck.append('joker')
    randomizer = random.choice(kleuren) + random.choice(kaarten)
    if randomizer not in deck:
        deck.append(randomizer)


for i in range(7):
    print(deck[i])
    deck.pop(i)

print(deck)