#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
cities = []
print("Anna viisi (5) kaupungin nimeä")
print("Voit lopettaa syötön painamalla ENTER")
city = input("Anna ensimmäinen kaupunki: ")
while city!="":
    cities.append(city)
    city = input("Anna seuraava kaupunki: ")
for n in cities:
    print (f"{n}")
