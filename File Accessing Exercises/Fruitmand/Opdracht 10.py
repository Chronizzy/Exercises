from fruitmand2 import fruitmand

gewicht = []
for i in fruitmand:
    gewicht.append(i['weight'])

gewicht.sort()

for i in gewicht:
    for j in fruitmand:
        if j['weight'] == i:
            print(j['name'].capitalize(),'weegt',  j['weight'], 'gram.')
