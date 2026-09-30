from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "Bem-vindo à API de Testes!"})

@app.route("/soma", methods=["GET"])
def rota_soma():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"resultado": a + b})
    except ValueError:
        return jsonify({"erro": "Parâmetros inválidos"}), 400

if __name__ == "__main__":
    app.run(debug=True)