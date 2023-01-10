import random

#namen = ['naam', 'naam1', 'naam2']
namen = []
loten = {}
keys = []
values = []


def test():
    while True:
        naamVraag = input('naam: ').lower()
        if naamVraag not in namen:
            namen.append(naamVraag)

        if len(namen) >= 3:
            ask = input('Wil je nog namen toevoegen? ja / nee: ')
            if (ask.lower()).startswith('n'):
                break
            else:
                continue
        
    while len(loten) != len (namen):
        if len(namen) - len(loten) == 2:
            for i in namen:
                for j in namen:
                    if i not in loten.keys():
                        if j not in  loten.values():
                            loten[i] = j
        for naam in namen:
            randomNaam = random.choice(namen)
            if naam != randomNaam and naam not in keys and randomNaam not in values:
                loten[naam] = randomNaam
                keys.append(naam)
                values.append(randomNaam)
            

    print('{----------}{-------------------}{----------}')
    for i, j in loten.items():
        print('         ', i.capitalize() , 'heeft', j.capitalize(), 'getrokken!')


test()
print('{----------}{-------------------}{----------}')