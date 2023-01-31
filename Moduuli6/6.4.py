#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
numbers = []
numbersint = []
def abc():
    #for element in numbers:
    #    numbersint.append(int(element))
    print(sum(numbers))


number = input("Anna kokonaisluku: ")
numbers.append(number)

while number != "":
    number = input("Anna seuraava kokonaisluku: ")
    numbers.append(number)
    if number:
        as_float = float(number)
    else:
        number = None
        print(abc())


