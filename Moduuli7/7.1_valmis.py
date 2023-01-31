#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
timeofyear = ("spring", "summer", "fall", "winter")

month = int(input("Syötä kuukauden numero kokonaislukuna"))

if month == 12 or month <= 2:
    timeofyear = timeofyear[3]
    print(f"Syötetty kuukausi on vuodenaikaa {timeofyear}")
elif month >= 3 and month <= 5:
    timeofyear = timeofyear[0]
    print(f"Syötetty kuukausi on vuodenaikaa {timeofyear}")
elif month >= 6 and month <= 8:
    timeofyear = timeofyear[1]
    print(f"Syötetty kuukausi on vuodenaikaa {timeofyear}")
elif month >= 9 and month <= 11:
    timeofyear = timeofyear[2]
    print(f"Syötetty kuukausi on vuodenaikaa {timeofyear}")
else:
    print("Virhe, et syöttänyt kokonaislukua tai se oli liian suuri")

