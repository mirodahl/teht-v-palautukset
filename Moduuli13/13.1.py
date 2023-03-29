#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, request, Response, jsonify

app = Flask(__name__)

def primer(num):
    Prime = True
    for i in range(2, num):
        if num % i == 0:
        Prime = False
    return Prime

@app.route("/prime/<int:n>")
def primed(num):
    result = primer(num)
    answer = {
        "number": num,
        "primed": result
    }
    return jsonify(answer)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)