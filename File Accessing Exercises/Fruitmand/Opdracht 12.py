from fruitmand2 import fruitmand

kleurenDictionary = {'pink' : 'roze', 'green' : 'groene', 'brown' : 'bruine', 'yellow' : 'gele', 'orange' : 'oranje', 'purple' : 'paarse', 'black' : 'zwarte'}

fruitnameLength = []
for i in fruitmand:
    fruitnameLength.append((len(i['name'])))
    fruitnameLength.sort(reverse = True)


for i in fruitmand:
    if fruitnameLength[0] == len(i['name']):
        print('De', i['name'], '( ' + str(fruitnameLength[0]) + 'letters )',  'heeft een', kleurenDictionary[i['color']], 'kleur en een gewicht van', (i['weight']) / 1000, 'kg' )

