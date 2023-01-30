#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
# vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.
multiplier = float(3.785)
appstate = True

print("Muunnan gallonoita litroiksi, voit poistua ohjelmasta syöttämällä negatiivisen määrän.")
gallons = int(input("Anna polttoainemäärä gallonoissa, muunnan litroiksi: "))
def converter():
    conversion = gallons * multiplier
    return float(conversion)

print("Annettu polttoainemäärä litroina: ")
print(converter())
if gallons > 0:
    gallons = int(input("Anna muunnettava polttoainemäärä: "))
    print(converter())
else:
    appstate = False



