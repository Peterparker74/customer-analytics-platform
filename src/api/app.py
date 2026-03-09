from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Charger le CSV final
df = pd.read_csv("data/processed/customers_final.csv")

# Route principale pour récupérer toutes les données
@app.route("/customers", methods=["GET"])
def get_customers():
    # Convertit le DataFrame en JSON
    data = df.to_dict(orient="records")
    return jsonify(data)

# Lancer le serveur
if __name__ == "__main__":
    app.run(debug=True, port=5000)
