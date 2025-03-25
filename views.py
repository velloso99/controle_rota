import sqlite3


# Criar conexão
try: 
    con = sqlite3.connect('calculo_rota.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conectar com Banco de Dados!")
    
# Tabela de de Lucro de Entregas--------------------------------------
def criar_dados(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO lucro_entregas(data, valor_rota, km_rodado, calculo, valor_combustivel, total_combustivel, total) values(?,?,?,?,?,?,?)"
        cur.execute(query, i)
        
def verificar_lucro(usuario):
    con = sqlite3.connect('calculo_rota.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM lucro_entregas WHERE usuario=?", (usuario,))
    resultado = cursor.fetchall()
    cursor.close()
    return bool(resultado)

def atualizar_lucro(i):
    with con:
        cur = con.cursor()
        query = "UPDATE lucro_entregas SET data=?, valor_rota=?, km_rodado=?, calculo=?, valor_combustivel=?, total_combustivel=?, total=? WHERE id=?"
        cur.execute(query, i)  # A variável 'dados' já é uma tupla
        con.commit()

        # Retorna True se a atualização for bem-sucedida
        return cur.rowcount > 0
    
def ver_lucro():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM lucro_entregas')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista

# deletar os  Cursos (Delete D)
def deletar_lucro(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM lucro_entregas WHERE id=? "
        cur.execute(query, i)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        