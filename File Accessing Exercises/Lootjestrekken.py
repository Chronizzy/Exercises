import random

loten = {}
namen = []
keys = []
values = []
keuze = 'ja'

while keuze == 'ja':
    if len(namen) < 3:
        keuze == 'ja'
    naamVraag = input('naam: ').lower()
    if naamVraag not in namen:
        namen.append(naamVraag)

    if len(namen) >= 3:
        ask = input('Wil je nog namen toevoegen? ja / nee ')
        if ask.lower() == 'nee':
            keuze = 'nee'
        

while len(loten) != len (namen):
    for naam in namen:
        randomNaam = random.choice(namen)
        if naam != randomNaam and naam not in keys and randomNaam not in values:
           loten[naam] = randomNaam
           keys.append(naam)
           values.append(randomNaam)
            

print(len(loten), loten)