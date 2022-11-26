from fruitmand1 import fruitmand

colors = []

for i in fruitmand:
    if i['name'] == 'druif':
        fruitmand.remove(i)

for i in fruitmand:
    if i['color'] not in colors:
        colors.append(i['color'])
        print(i['color'])   