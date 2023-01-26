#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun
# väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
diceresult = 0
print("Heitän noppaa niin kauan kunnes saan silmäluvun 6")


def noppa():
    random.randint(1, 6)

while diceresult < 1:
    if noppa < 6:
        print(noppa())
        diceresult = 0
    else:
        print(noppa())
        diceresult = diceresult + 1