##Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
##Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
##Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta. pinta-ala kanta*korkeus
##
import math

height_str = input("Anna suorakulmion kannan pituus: ")
height = int(height_str)

base_str = input("Anna suorakulmion korkeus: ")
base = int(base_str)

area = height * base
circle = height + height + base + base

print("Suorakulmion piiri on: ")
print(circle)

print("Suorakulmion pinta-ala on:")
print(area)