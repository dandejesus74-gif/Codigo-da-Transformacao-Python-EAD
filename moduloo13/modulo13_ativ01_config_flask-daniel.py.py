from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Olá! Bem-vindo à API Flask."})

if __name__ == "__main__":
    print("A iniciar o servidor Flask para o Passo 1...")
    app.run(debug=True)