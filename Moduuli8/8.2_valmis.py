#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
# kyseisessä maassa
# olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )

def search_airports(countrycode):
    sql = "SELECT type, count(*)" + \
          "FROM airport " + \
          "WHERE iso_country='" + countrycode + "'" "GROUP by type"

    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    print(tabulate(tulos, headers=['Tyyppi', 'Määrä'], tablefmt='psql'))
    return

countrycode = input("Anna maatunnus: ")
print(search_airports(countrycode))

connection.close()