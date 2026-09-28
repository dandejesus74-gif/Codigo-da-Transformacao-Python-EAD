import sqlite3

def inicializar_bd():
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    """)
    conn.commit()
    conn.close()

def adicionar_tarefa(titulo):
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Tarefas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    conn.close()
    print(f"Tarefa '{titulo}' adicionada!")

def visualizar_tarefas():
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    
    print("\n--- Minhas Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for t in tarefas:
        print(f"[{t[0]}] {t[1]} - Status: {t[2]}")

def excluir_tarefa(tarefa_id):
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (tarefa_id,))
    conn.commit()
    conn.close()
    print(f"Tarefa ID {tarefa_id} excluída!")

# Exemplo de uso do Gerenciador de Tarefas
if __name__ == "__main__":
    inicializar_bd()
    
    # Adicionar
    adicionar_tarefa("Estudar Python")
    adicionar_tarefa("Fazer o módulo 11")
    
    # Visualizar
    visualizar_tarefas()
    
    # Excluir
    excluir_tarefa(1)
    
    # Visualizar novamente
    visualizar_tarefas()