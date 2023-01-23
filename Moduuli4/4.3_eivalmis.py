#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

numbers = []
print("Anna minulle lukuja. Keskeytä painamalla ENTER.")
print("Lopuksi tulostan isoimman ja pienimmän antamasi luvut.")
num = input("Anna luku: ")
while num != "":
    numbers.append(num)
    num = input("Anna halutessasi uusi luku tai keskeytä painamalla ENTER: ")
for i in range (numbers):
    print("Suurin :", max(numbers), "\nPienin :", min(numbers))
