#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy import distance
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )

print("Tarkistan kahden haluamasi kentän välisen etäisyyden")
ICAO = input("Anna ensimmäisen kentän ICAO-koodi: ")
ICAO2 = input("Anna verrattavan kentän ICAO-koodi:")

sql = "SELECT longitude_deg, latitude_deg " +\
          "FROM airport " +\
          " WHERE ident='" + ICAO + "'"
print(sql)
kursori = connection.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
if kursori.rowcount > 0:
    for row in tulos:
        print(f"{row[0]}, {row[1]}")
sql = "SELECT longitude_deg, latitude_deg " +\
          "FROM airport " +\
          " WHERE ident='" + ICAO2 + "'"
print(sql)
kursori = connection.cursor()
kursori.execute(sql)
tulos2 = kursori.fetchall()
if kursori.rowcount > 0:
    for rivi in tulos2:
        print(f"{rivi[0]}, {rivi[1]}")
def distancecalculator():
    yksi = (row[0], row[1])
    kaksi = (rivi[0], rivi[1])
    print(distance.distance(yksi, kaksi).miles)

print("Hakemiesi kenttien etäisyys maileissa:")
print(distancecalculator())

connection.close()