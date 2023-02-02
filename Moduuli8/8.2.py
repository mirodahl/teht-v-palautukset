#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
# kyseisessä maassa
# olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )

def search_airports(iso_country):
    sql = "SELECT type " +\
          "FROM airport " +\
          " WHERE iso_country='" + iso_country + "'"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"ICAO-koodilla löytynyt kenttä on {rivi[0]} ja sen sijainti on {rivi[1]}")
    return

iso_country = input("Anna ICAO-koodi: ")
print(search_airports(iso_country))

connection.close()