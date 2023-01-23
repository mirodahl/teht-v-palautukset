#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random
player_number = int(input("Valitse kokonaisluku väliltä 1 - 10: "))
ai_guess = random.randint(1, 10)
number_known = False
if int(player_number) > 10:
    print("Luku pitää olla väliltä 1-10, syötä uusi luku!")
    player_number = int(input("Syötä uusi luku OIKEIN: "))
else:
    while number_known == False:
        if ai_guess == player_number:
            print(f"Oikein. Numerosi oli {ai_guess}")
            number_known = True
        elif ai_guess >= player_number:
            print(f"Liian suuri arvaus, arvasin {ai_guess}")
            player_number = int(input("Valitse uusi luku: "))
        else:
            print(f"Liian pieni arvaus, arvasin {ai_guess}")
            player_number = int(input("Valitse uusi luku: "))
            if number_known == True:
                break
