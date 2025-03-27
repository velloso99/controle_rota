from imports import *
from tkinter import messagebox
import sqlite3


# Criar conexão
try: 
    con = sqlite3.connect('calculo_rota.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conectar com Banco de Dados!")
    
# Tabela de de Lucro de Entregas--------------------------------------
def criar_dados(lista):
    conn = sqlite3.connect("calculo_rota.db")
    cursor = conn.cursor()
    
    # Verifica se os dados já existem
    cursor.execute("SELECT COUNT(*) FROM lucro_entregas WHERE data=? AND valor_rota=? AND km_rodado=?", (lista[0], lista[1], lista[2]))
    if cursor.fetchone()[0] > 0:
        messagebox.showwarning("Aviso", "Esse registro já existe no banco de dados!")
        conn.close()
        return

    # Inserindo os dados
    cursor.execute("INSERT INTO lucro_entregas (data, valor_rota, km_rodado, calculo, valor_comb, total_comb, total_lucro) VALUES (?, ?, ?, ?, ?, ?, ?)", lista)
    conn.commit()
    conn.close()

def atualizar_lucro(i):
    with con:
        cur = con.cursor()
        query = "UPDATE lucro_entregas SET data=?, valor_rota=?, km_rodado=?, calculo=?, valor_combustivel=?, total_combustivel=?, total=? WHERE id=?"
        cur.execute(query, i)  # A variável 'dados' já é uma tupla
        con.commit()

        # Retorna True se a atualização for bem-sucedida
        return cur.rowcount > 0
    
def ver_lucro():
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM lucro_entregas')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar lista: {e}")
        return []
# deletar os  Cursos (Delete D)
def deletar_lucro(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM lucro_entregas WHERE id=? "
        cur.execute(query, i)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        