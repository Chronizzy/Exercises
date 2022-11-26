from fruitmand1 import fruitmand

for i in fruitmand[::-1]:
    if i['name'] == 'appel':
        print('De', i['name'], 'weegt', i['weight'], 'gram.')