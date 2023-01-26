#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.
#import random
import numpy as np
dices = []
dicesgiven = 0
while dicesgiven == 0:
    diceReq = int(input("Anna arpakuutioiden määrä: "))
    dices.append(diceReq)
    dicesgiven = dicesgiven + 1
    dice = dices[0]
    if dicesgiven == 1:
        for i in range(0, len(dices)):
            print(sum(list(np.random.randint(low=1, high=6, size=diceReq))))


