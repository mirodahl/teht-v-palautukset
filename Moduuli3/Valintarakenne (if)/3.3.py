#Kirjoita ohjelma, jokakysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
#Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

gender = input("Syötä sukupuoli, 1 = mies, 2 = nainen: ")
hg = int(input("Syötä hemoglobiiniarvo g/l: "))
if gender == 1:
    print("Hemoglobiini on normaali")
elif gender == 1 and (int(hg) <= 133):
    print("Hemoglobiini on alhainen")
elif gender == 1 and (int(hg) >= 196):
    print("Hemogblobiini on korkea")
elif gender == 2:
    print("Hemoglobiini on normaali")
elif gender == 2 and (int(hg) <= 116):
    print("Hemoglobiini on alhainen")
elif gender == 2 and (int(hg) >= 176):
    print("Hemogblobiini on korkea")

