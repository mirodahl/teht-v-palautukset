##Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan
##leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja
##grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
##Yksi leiviskä on 20 naulaa.
##Yksi naula on 32 luotia.
##Yksi luoti on 13,3 grammaa.

print("Anna massa seuraavaksi pyydetyillä mitoilla.")
talent_str = input("Leiviskät: ")
bolt_str = input("Naulat: ")
bullet_str = input("Luodit: ")

talent = int(talent_str) * 13.3 * 32 * 20
bolt = int(bolt_str) * 13.3 * 32
bullet = int(bullet_str) * 13.3

raw_mass = int(talent) + int(bolt) + int(bullet)
mass_g1 = int(raw_mass)
mass_g2 = int(mass_g1)
mass_kg = int(mass_g2) * 0.001

print("Antamiesi massojen perusteella kokonaismassa grammoina on: ")
print(mass_g1)
print("ja kilogrammoina: ")
print(mass_kg)