from fruitmand2 import fruitmand

kleurenDictionary = {'pink' : 'roze', 'green' : 'groene', 'brown' : 'bruine', 'yellow' : 'gele', 'orange' : 'oranje', 'purple' : 'paarse', 'black' : 'zwarte'}

info = []
for i in fruitmand:
    info.append((len(i['name'])))
    info.sort(reverse = True)


for i in fruitmand:
    if info[0] == len(i['name']):
        print('De', i['name'], '( ' + str(info[0]) + 'letters )',  'heeft een', kleurenDictionary[i['color']], 'kleur en een gewicht van', (i['weight']) / 1000, 'kg' )

