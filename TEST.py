
namen = []
leeftijden = []
a = 0
vraag = True

def namen_leeftijden(w):
    if w:
        naam = input("Voer een naam in:\nOf voer stop in om te stoppen:\n>>> ")
        if naam == "stop":
            vraag = False
            pass
        leeftijd = input("Voer een leeftijd in: ")
        namen.append(naam)
        leeftijden.append(leeftijd)
        return{'naam':naam, 'leeftijd':leeftijd}
    else: 
        pass


while vraag:
    namen_leeftijden(vraag)
    
for i in namen:
    print(f'{i} is {leeftijden[a]} jaar')
    a +=1
