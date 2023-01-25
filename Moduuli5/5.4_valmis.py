#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
cities = []
cityamount = 0
print("Anna viisi (5) kaupungin nimeä")
city = input("Anna ensimmäinen kaupunki: ")
cities.append(city)
cityamount = cityamount + 1
while cityamount < 5:
    city = input("Anna seuraava kaupunki: ")
    cities.append(city)
    cityamount = cityamount + 1

for i in range(0, len(cities)):
    print(cities[i])
