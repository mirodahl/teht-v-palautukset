#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun
# väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
diceresult = 0
print("Heitän noppaa niin kauan kunnes saan silmäluvun 6")


def noppa():
    return random.randint(1, 6)

result = noppa()
while result != 6:
    print("Heitän uudestaan")
    result = noppa()
    if result == 6:
        print(result)
        result = noppa()
        break