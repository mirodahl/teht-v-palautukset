#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

print("Aloitetaan!")
username = input("Syötä käyttäjänimesi: ")
password = input("Syötä salasanasi: ")
tries = 0
while tries < 5:
    if username == 'python' and password == 'rules':
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty.")
        tries = tries + 1
        if tries < 5:
            username = input("Syötä käyttäjänimesi: ")
            password = input("Syötä salasanasi: ")

