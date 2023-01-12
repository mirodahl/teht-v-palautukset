##Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
##kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
##nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
##Vihje: tutustu random.randint()-funktion käyttöön.
import random

a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = random.randint(1,6)
e = random.randint(1,6)
f = random.randint(1,6)
g = random.randint(1,6)

print(str(a) + str(b) + str(c))
print(str(d) + str(e) + str(f) + str(g))