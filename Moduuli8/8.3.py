#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )

def search_airports(ICAO):
    sql = "SELECT name, municipality " +\
          "FROM airport " +\
          " WHERE ident='" + ICAO + "'"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"ICAO-koodilla löytynyt kenttä on {rivi[0]} ja sen sijainti on {rivi[1]}")
    return

ICAO = input("Anna ICAO-koodi: ")
print(search_airports(ICAO))

connection.close()