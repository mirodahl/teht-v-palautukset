##Kirjoita ohjelma, joka kysyy kolme kokonaislukua
##Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
one_str = input('Anna ensimmäinen kokonaisluku: ')
one = int(one_str)

two_str = input('Anna toinen kokonaisluku: ')
two = int(two_str)

three_str = input('Anna kolmas kokonaisluku: ')
three = int(three_str)

sum = one+two+three
product = one*two*three
average = (one+two+three)/3

print("Lukujen summa on:")
print(sum)

print("Lukujen tulo on:")
print(product)

print("Lukujen keskiarvo on:")
print(average)