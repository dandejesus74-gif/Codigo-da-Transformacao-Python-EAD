import sqlite3

def filtrar_clientes_com_a():
    conexao = sqlite3.connect("sistema.db")
    cursor = conexao.cursor()
    
    # Filtro SQL para nomes que começam com "A"
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")
    clientes = cursor.fetchall()
    conexao.close()
    
    print("\n--- Passo 3: Clientes com nome começando em 'A' ---")
    if not clientes:
        print("Nenhum cliente encontrado com a letra 'A'. (Cadastre algum para testar!)")
    for c in clientes:
        print(f"ID: {c[0]} | Nome: {c[1]} | E-mail: {c[2]}")
    print("-" * 45)

if __name__ == "__main__":
    # Dica: Certifique-se de inserir clientes que comecem com 'A' (ex: Ana, Arthur) para ver o filtro funcionando
    filtrar_clientes_com_a()