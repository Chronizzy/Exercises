
formuleStof = input('Welke stof wil je de isomeren van weten? ')
#formuleStof = 'c6h12'

C_atoms = ''
H_atoms = ''

for i in formuleStof:
    if i.lower() == 'c':
        for j in range (1, formuleStof.find('h')):
            if formuleStof[formuleStof.find('c') + j] != 'h':
                C_atoms += formuleStof[formuleStof.find('c') + j]

    if i.lower() == 'h':
        for j in range(formuleStof.find('h') - 1, len(formuleStof) - len(C_atoms) - 1):
            if formuleStof[formuleStof.find('h') + j] != 'c':
                H_atoms += formuleStof[formuleStof.find('h') + j]
            else:
                break


print('Aantal C atomen: ', C_atoms, 'en aantal H atomen: ' ,H_atoms)


