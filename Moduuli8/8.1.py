import mysql.connector

def searchAirports(ICAO):
    sql = "SELECT Numero, Sukunimi, Etunimi, Palkka FROM airports"
    sql += " WHERE ICAO='" + ICAO + "'"
    print(sql)
    kursori = yhteys.cursor()
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
         user='dbuser',
         password='sAL_a3ana',
         autocommit=True
         )

ICAO = input("Anna ICAO-koodi: ")
searchAirports(ICAO)