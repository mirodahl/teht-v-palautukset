import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )

def haeTyöntekijätSukunimellä(sukunimi):
    sql = "SELECT Numero, Sukunimi, Etunimi, Palkka FROM Työntekijä"
    sql += " WHERE Sukunimi='" + sukunimi + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return


sukunimi = input("Anna sukunimi: ")
haeTyöntekijätSukunimellä(sukunimi)