#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja
# kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
import mysql.connector
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game_og',
         user='user1',
         password='sala1',
         autocommit=False
         )

def search_airports(ICAO):
    sql = "SELECT name, municipality " +\
          "FROM airport " +\
          " WHERE ident='" + ICAO + "'"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
#    if kursori.rowcount > 0:
#        for rivi in tulos:
#            print(f"ICAO-koodilla löytynyt kenttä on {rivi[0]} ja sen sijainti on {rivi[1]}")
    return
def get_data_from_db():
    pass
@app.route('/airporter')
def airporter():
    request = "http://127.0.0.1:3000/port/" + ICAO
    answer = requests.get(request).json()
    return print(answer)

@app.errorhandler(404)
def page_not_found(status):
    res = {"status": "404", "message": "Not found"}
    res_json = json.dumps(res)
    return Response(response=res_json, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)