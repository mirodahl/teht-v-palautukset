#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.
import random
dice_amount = []
dice_amounts = dice_amount
dice_sides = 6
dice_request = int(input("Kuinka montaa noppaa heitämme? Lasken jokaisen nopan lukujen summan. Paina sen jälkeen ENTER jatkaaksesi."))
while dice_request!="":
    dice_amount.append(dice_request)
    dice_request = input("Paina ENTER jatkaaksesi.")
    def dice_roll(dice_amounts,dice_sides):
        for i in range (0,dice_amounts):
            die = random.randint(1, 6)
            yield die
for num in range(0):
    print(f"{dice_roll}")
#    def dice_roll(dice_amounts,dice_sides):
#        for i in range (0,dice_amounts):
#            die = random.randint(1, 6)
#            yield die
#for num in range(1):
#    print("Heitettyjen noppien määrä")
#    print(f"{num}")
#    generator = dice_roll(dice_amounts,dice_sides)
#    print(sum(generator))