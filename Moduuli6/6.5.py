#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
# paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen
# sekä alkuperäisen että karsitun listan.
numbers = []
def abc():
    print(numbers)


number = input("Anna kokonaisluku: ")
numbers.append(number)

while number != "":
    number = input("Anna seuraava kokonaisluku: ")
    numbers.append(number)

print(abc())