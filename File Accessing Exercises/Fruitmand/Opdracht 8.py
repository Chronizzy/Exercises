from fruitmand1 import fruitmand

fruitmand.append({'name': 'watermelon', 'weight': 14000, 'color': 'green/red', 'round': True})

weighttotal = 0
for i in fruitmand:
    weighttotal += i['weight']
    
print(weighttotal)