import sqlite3

def conectar():
    return sqlite3.connect("sistema.db")

def criar_tabela_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_tarefa(descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conexao.commit()
    conexao.close()
    print(f"Tarefa adicionada: '{descricao}'")

def visualizar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    
    print("\n--- Gerenciamento de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for t in tarefas:
        print(f"ID [{t[0]}] - {t[1]}")
    print("-" * 32)

def excluir_tarefa(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()
    conexao.close()
    print(f"Tarefa ID {id_tarefa} excluída com sucesso!")

if __name__ == "__main__":
    criar_tabela_tarefas()
    
    print("Desafio Extra: Sistema de Tarefas")
    adicionar_tarefa("Completar o módulo de SQLite")
    adicionar_tarefa("Fazer commit no GitHub")
    
    visualizar_tarefas()
    
    # Exemplo de exclusão:
    # excluir_tarefa(1)