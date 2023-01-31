#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

pizzawidth1 = int(input("Ensimmäisen pitsan halkaisija: "))
pizzaprice1 = int(input("Ensimmäisen pitsan hinta: "))
pizzawidth2 = int(input("Toisen pitsan halkaisija: "))
pizzaprice2 = int(input("Toisen pitsan hinta: "))

def pizzavalue():
    pizzavalue1 = pizzawidth1 / pizzaprice1
    pizzavalue2 = pizzawidth2 / pizzaprice2
    if pizzavalue1 > pizzavalue2:
        print("Ensimmäinen pitsa on parempaa vastinetta rahalle")
    elif pizzavalue2 > pizzavalue1:
        print("Toinen pitsa on parempaa vastinetta rahalle")
    else:
        print("Pitsat ovat yhtä hyvä vastine rahalle")

print(pizzavalue())