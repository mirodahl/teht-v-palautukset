#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot
# vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
def airport_add():
    callsign = input("Anna lentokentän tunnus: ")
    name = input("Anna lentokentän nimi: ")
    airports[callsign] = name
    return
def airport_search():
    callsign = input("Anna lentokentän ICAO-koodi: ")
    if callsign in airports:
        print(f"{airport}")
    else:
        print("Lentokenttää ei löydy")
    return
def airport_details():
    for airport in airports:
        print(f"{airport}")
    return

airports = {"EFHK" : "Helsinki-Vantaan lentoasema",
            "EFET" : "Enontekiön lentoasema",
            "EFIV" : "Ivalon lentoasema",
            "EFKI" : "Kajaanin lentoasema"}

appstate = True
userfunction = -1

while userfunction != 3:
    print("0 = Selaa tallennettuja ICAO-tunnuksia")
    print("1 = lisää uusi lentokenttä")
    print("2 = hae lentokenttä ICAO-koodilla")
    print("3 = lopeta")

    userfunction = int(input("Valitse toiminto: "))
    if userfunction == 0:
        airport_details()
    elif userfunction == 1:
        airport_add()
    elif userfunction == 2:
        airport_search()
    else:
        print("näkemiin")