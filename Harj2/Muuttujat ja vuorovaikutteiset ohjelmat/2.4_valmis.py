##Kirjoita ohjelma, joka kysyy kolme kokonaislukua
##Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
yksi_str = input('Anna ensimmäinen kokonaisluku: ')
yksi = float(yksi_str)

kaksi_str = input('Anna toinen kokonaisluku: ')
kaksi = float(kaksi_str)

kolme_str = input('Anna kolmas kokonaisluku: ')
kolme = float(kolme_str)

summa = yksi*kaksi*kolme
tulo = yksi+kaksi+kolme
karvo1 = yksi+kaksi+kolme
karvo2 = karvo1/3

print("Lukujen summa on:")
print(summa)

print("Lukujen tulo on:")
print(tulo)

print("Lukujen keskiarvo on:")
print(karvo2)