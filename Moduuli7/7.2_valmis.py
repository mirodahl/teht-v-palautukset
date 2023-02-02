#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.
#import random

names = set()

print("Kyselen sinulta nimiä. Voit lopettaa ohjelman suorittamisen, syöttämällä tyhjän.")
name = input("Anna nimi: ")

while name != "":
    if name in names:
        print("Nimi syötetty aikaisemmin")
    else:
        print("Uusi nimi tallennettu")
        names.add(name)
    name = input("Anna uusi nimi: ")

#random.shuffle(names)
print(names)