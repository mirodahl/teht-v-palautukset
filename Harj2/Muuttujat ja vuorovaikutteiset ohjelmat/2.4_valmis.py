##Kirjoita ohjelma, joka kysyy kolme kokonaislukua
##Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
one_str = input('Anna ensimmäinen kokonaisluku: ')
one = float(one_str)

two_str = input('Anna toinen kokonaisluku: ')
two = float(two_str)

three_str = input('Anna kolmas kokonaisluku: ')
three = float(three_str)

sum = one+two+three
product = one*two*three
average1 = one+two+three
average2 = average1/3

print("Lukujen summa on:")
print(sum)

print("Lukujen tulo on:")
print(product)

print("Lukujen keskiarvo on:")
print(average2)