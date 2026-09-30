import sqlite3

def conectar():
    return sqlite3.connect("sistema.db")

def inserir_cliente(nome, email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    print(f"[{nome}] inserido com sucesso!")

def consultar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexao.close()
    
    print("\n--- Consulta de Clientes ---")
    for c in clientes:
        print(f"ID: {c[0]} | Nome: {c[1]} | E-mail: {c[2]}")
    print("-" * 30)

def atualizar_cliente(id_cliente, novo_nome, novo_email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id_cliente))
    conexao.commit()
    conexao.close()
    print(f"Cliente ID {id_cliente} atualizado!")

def deletar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    conexao.close()
    print(f"Cliente ID {id_cliente} deletado!")

if __name__ == "__main__":
    print("Passo 2: Testando operações CRUD")
    inserir_cliente("Bruno Silva", "bruno@email.com")
    inserir_cliente("Carla Dias", "carla@email.com")
    
    consultar_clientes()
    
    atualizar_cliente(1, "Bruno Silva Santos", "bruno.santos@email.com")
    consultar_clientes()
    
    # Descomente a linha abaixo se quiser testar a exclusão
    # deletar_cliente(2)