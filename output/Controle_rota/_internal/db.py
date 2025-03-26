import sqlite3


# Criar conexão
try: 
    con = sqlite3.connect('calculo_rota.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conectar com Banco de Dados!")

# Criar tabelas do Banco de Dados
# Tabela de Login--------------------------------------
try:
    with con:
        cur = con.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lucro_entregas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                valor_rota TEXT,
                km_rodado TEXT,
                calculo TEXT,
                valor_combustivel TEXT,
                total_combustivel TEXT,
                total TEXT
            )""")
        print("Tabela de lucro_entregas criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela de lucro_entregas!")


    







