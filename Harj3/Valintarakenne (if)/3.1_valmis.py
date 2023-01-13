##Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
##Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
## montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
##Kuha on alamittainen, jos sen pituus on alle 37 cm.

print("Tarkistetaan ettei kuhasi ole alamittainen!")
fish = float(input("Syötä saamasi kuhan pituus senttimetreinä: "))

if fish>=37:
    print("Kuhasi on tarpeeksi suuri.")

if fish<=37:
    undersize = 37 - fish
    print(f"Kuhasi on {undersize}cm alamittainen, laske se takaisin järveen!")
