##Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
##Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
##Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta. pinta-ala kanta*korkeus
##
import math

height = input("Anna suorakulmion kannan pituus: ")
base = input("Anna suorakulmion korkeus: ")

area = height * base
circle = height + height + base + base
