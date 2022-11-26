from fruitmand2 import fruitmand
import random

kleuren = []

for i in fruitmand:
    if i['color'] not in kleuren:
        kleuren.append(i['color'])

kleurVraag = input(f'Kies een kleur uit het volgende: {kleuren}')

while kleurVraag not in kleuren:
    print(f'De kleur {kleurVraag} zit niet in de mand')
    kleurVraag = input(f'Kies een kleur uit het volgende: {kleuren}')

rondeVruchten = 0
nietrondeVruchten = 0

for i in fruitmand:
    if i['color'] == kleurVraag:
        if i['round'] == True:
            rondeVruchten += 1
        else:
            nietrondeVruchten += 1

if rondeVruchten > nietrondeVruchten:
    print(f'Er zijn {rondeVruchten-nietrondeVruchten} meer ronde vruchten dan niet ronde vruchten in de kleur {kleurVraag}.')
if rondeVruchten < nietrondeVruchten:
    print(f'Er zijn {nietrondeVruchten-rondeVruchten} minder ronde vruchten dan niet ronde vruchten in de kleur {kleurVraag}.')
if rondeVruchten == nietrondeVruchten:
    print(f'Er zijn {rondeVruchten} ronde vruchten en {nietrondeVruchten} niet ronde vruchten in de kleur {kleurVraag}.')