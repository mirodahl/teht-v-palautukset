import mysql.connector

def searchAirports(ICAO):
    sql = "SELECT Name, Municipality FROM Airports"
    sql += " WHERE ident='" + ICAO + "'"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='airports',
         user='user1',
         password='sala1',
         autocommit=True
         )

ICAO = input("Anna ICAO-koodi: ")
searchAirports(ICAO)