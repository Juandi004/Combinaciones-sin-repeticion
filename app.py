from flask import Flask, render_template, request
from itertools import combinations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    combinaciones = []
    if request.method == "POST":
        elementos = request.form["elementos"]
        longitud = int(request.form["longitud"])

        
        elementos = list(set(elementos.split()))
        
       
        combinaciones = list(combinations(elementos, longitud))

    return render_template("index.html", combinaciones=combinaciones)

if __name__ == "__main__":
    app.run(debug=True)
