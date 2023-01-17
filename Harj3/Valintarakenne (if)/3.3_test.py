##Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
##Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

##Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
##Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

gender = int(input("Syötä sukupuoli, 1 = mies, 2 = nainen: "))
hg = int(input("Syötä hemoglobiiniarvo g/l: "))

if (gender == 1) and (134 >= hg <= 195):
    print("Hemoglobiini on normaali")
elif (gender == 1) and (hg < 134):
    print("Hemoglobiini on alhainen")
elif (gender == 1) and (hg > 195):
    print("Hemogblobiini on korkea")
