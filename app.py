from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False

COLIS = {
    "GT-1001": {"client": "SOTELGAB", "statut": "En transit", "ville": "Libreville","poids_kg": 120},
    "GT-1002": {"client": "TRANSGABON", "FRET": "Livré", "ville": "Libreville"},
    
}

@app.route("/health")
def health():
   return jsonify(status="ok"), 200

@app.route("/colis/<ref>")
def get_colis(ref):
    if ref in COLIS:
        return jsonify(COLIS[ref]), 200
    else:
        return jsonify({"error": "Colis introuvable  dans le systeme"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)