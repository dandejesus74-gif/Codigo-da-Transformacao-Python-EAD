from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    
    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Dados incompletos. Envie 'nome' e 'email'."}), 400
    
    nome = dados.get("nome")
    email = dados.get("email")
    
    return jsonify({
        "mensagem": "Dados recebidos com sucesso!",
        "utilizador": {
            "nome": nome,
            "email": email
        }
    }), 201

if __name__ == "__main__":
    print("A iniciar o servidor Flask para o Passo 2...")
    app.run(debug=True)