from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def inicializar_banco_blog():
    conexao = sqlite3.connect("blog.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

# Função simples de autenticação por token no cabeçalho (Header: Authorization)
def verificar_autenticacao():
    token = request.headers.get("Authorization")
    # Token de exemplo para validação
    return token == "Bearer token_secreto_123"

@app.route("/posts", methods=["POST"])
def criar_post():
    if not verificar_autenticacao():
        return jsonify({"erro": "Não autorizado. Token inválido ou ausente."}), 401
    
    dados = request.get_json()
    if not dados or "titulo" not in dados or "conteudo" not in dados:
        return jsonify({"erro": "Título e conteúdo são obrigatórios."}), 400
    
    titulo = dados.get("titulo")
    conteudo = dados.get("conteudo")
    
    conexao = sqlite3.connect("blog.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO posts (titulo, conteudo) VALUES (?, ?)", (titulo, conteudo))
    conexao.commit()
    conexao.close()
    
    return jsonify({"mensagem": "Post criado com sucesso!"}), 201

@app.route("/posts", methods=["GET"])
def listar_posts():
    conexao = sqlite3.connect("blog.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conexao.close()
    
    lista_posts = [{"id": p[0], "titulo": p[1], "conteudo": p[2]} for p in posts]
    return jsonify(lista_posts), 200

if __name__ == "__main__":
    inicializar_banco_blog()
    print("A iniciar a API do Blog...")
    app.run(debug=True)