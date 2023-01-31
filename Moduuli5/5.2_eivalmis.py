#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
numbers = []

#numbers_amount = 0

number_Str = input("Anna ensimmäinen luku tai lopeta painamalla Enter: ")
# = numbers_amount + 1
while number_Str != "":
    number = int(number_Str)
    numbers.append(number)
    number_Str = input("Anna seuraava luku tai lopeta painamalla Enter: ")
    #numbers_amount = numbers_amount + 1
for i in range(0, 5):
    numbers.sort(reverse=True)
    print(numbers[i]) #toimii muuten, mutta esim. antamalla luvut 1-6 ohjelma ei tulosta 65432 vaikka sort on käännetty