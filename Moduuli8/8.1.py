import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )

def searchAirports(ICAO):
    sql = "SELECT name, municipality" +\
          "FROM airport"
    sql += " WHERE ident='" + ICAO + "'"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"ICAO-koodilla löytynyt kenttä on {rivi[0]} ja sen sijainti on {rivi[1]}")
    return

ICAO = input("Anna ICAO-koodi: ")
print(searchAirports(ICAO))

connection.close()