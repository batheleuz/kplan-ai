
### app.py ###
from flask import Flask, request, jsonify, render_template
from main import get_response

# Initialisation de l'application Flask
app = Flask(__name__)

# Route principale pour afficher la page HTML
@app.route("/")
def sql_page():
    return render_template('index.html')

# Route pour gérer les requêtes de chat
@app.route("/chat", methods=["POST"])
def text2sqlchat():
    user_query = request.form.get("text")
    
    if not user_query:
        return jsonify({"text": "Requête invalide"})

    # Appeler directement get_response
    response = get_response(user_query)

    return jsonify({"text": response["response"], "sources": response["sources"]})

# Lancer l'application Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)