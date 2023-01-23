#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
numbers = []
numbers.sort(reverse=True)
numbers_amount = 0

number = input("Anna ensimmäinen luku tai lopeta painamalla Enter: ")
numbers_amount = numbers_amount + 1
while number!="":
    numbers.append(number)
    number = input("Anna seuraava luku tai lopeta painamalla Enter: ")
    numbers_amount = numbers_amount + 1
for n in numbers:
    if numbers_amount > 5:
        print(numbers[4])
        print(numbers[3])
        print(numbers[2])
        print(numbers[1])
        print(numbers[0])
    else:
        print(f"{n}")