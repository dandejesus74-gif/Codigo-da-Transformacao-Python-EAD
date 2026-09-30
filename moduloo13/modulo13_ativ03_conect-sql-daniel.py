from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def inicializar_banco():
    conexao = sqlite3.connect("banco_api.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilizadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

@app.route("/cadastrar", methods=["POST"])
def cadastrar_com_sqlite():
    dados = request.get_json()
    
    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Dados incompletos. Envie 'nome' e 'email'."}), 400
    
    nome = dados.get("nome")
    email = dados.get("email")
    
    # Persistir no SQLite
    conexao = sqlite3.connect("banco_api.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO utilizadores (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    
    return jsonify({"mensagem": "Utilizador cadastrado e gravado no SQLite com sucesso!"}), 201

if __name__ == "__main__":
    inicializar_banco()
    print("A iniciar o servidor Flask para o Passo 3...")
    app.run(debug=True)