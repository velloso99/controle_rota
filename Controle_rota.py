from imports import *




#Criando a janela
root = tk.Tk()
root.title("Controle de Estoque")
root.geometry("900x900")
root.configure(background=co0)
root.resizable(width=False, height=False)
largura_root = 900
altura_root = 900
#obter tamanho da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

Style = Style(root)
Style.theme_use("clam")
Style.configure("green.Horizontal.TProgressbar", 
                foreground="green", 
                background="green")

#**********************CRIANDO FRAME********************************
f_titulo = Frame(root, width=900, height=50, bg=co0)
f_titulo.grid(row=0 , column=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

f_botoes = Frame(root, width=900, height=65, bg=co0)
f_botoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

f_painel = Frame(root, width=900, height=393, bg=co0)
f_painel.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=5, columnspan=1, ipadx=680)

f_tabela= Frame(root, width=850, height=200, bg=co0)
f_tabela.grid(row=6, column=0, pady=0, padx=10, sticky=NSEW)
#**********************CRIANDO CONFIGURAÇÃO********************************
# Função para pegar a data selecionada
def calendario():
    
    def pegar_data():
        data_selecionada = cal.selection_get()  # Obtém a data selecionada
        entry_data.delete(0, END)  # Limpa o Entry
        entry_data.insert(0, data_selecionada.strftime("%d/%m/%Y"))  # Insere a data formatada no Entry
        calendario_root.destroy()  # Fecha o calendário

    calendario_root = tk.Toplevel(root)  # Cria uma nova janela
    calendario_root.title("Selecionar Data")
    calendario_root.resizable(width=False, height=False)
    largura_root = 200
    altura_root = 270
    #obter tamanho da tela
    largura_tela = calendario_root.winfo_screenwidth()
    altura_tela = calendario_root.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root )//2
    pos_y = (altura_tela - altura_root)//2
    # Definir geometria da janela (LxA+X+Y)
    calendario_root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")
    cal = Calendar(calendario_root, selectmode="day", date_pattern="dd/mm/yyyy")  # Cria o calendário
    cal.pack(pady=20)
    Button(calendario_root, text="Selecionar", command=pegar_data).pack(pady=10)  # Botão para selecionar a data
        


#**********************CRIANDO LABEL********************************


l_titulo = Label(f_titulo, text="Cadastro de rotas", font=('Ivy 20 bold'), bg=co0, fg=co1)
l_titulo.place(x=430, y=23, anchor=CENTER)


l_id = Label(f_painel, text="id:", font=('Ivy 10 bold'), bg=co0, fg=co1)
l_id.place(x=10, y=10)
e_id= Entry(f_painel, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_id.place(x=40, y=10)

bt_calendario = Button(f_painel, text="Data", command=calendario)
bt_calendario.place(x=10, y=40)
entry_data = Entry(f_painel, width=10, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
entry_data.place(x=70, y=40) 

l_valor_rota = Label(f_painel, text="Valor da Rota (R$):", font=('Ivy 10 bold'), bg=co0, fg=co1)
l_valor_rota.place(x=10, y=70)
e_valor_rota= Entry(f_painel, width=15, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_valor_rota.place(x=135, y=70)

l_km_rodado = Label(f_painel, text="Km Rodado (KM):", font=('Ivy 10 bold'), bg=co0, fg=co1)
l_km_rodado.place(x=10, y=100)
e_km_rodado= Entry(f_painel, width=15, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_km_rodado.place(x=135, y=100)

l_valor_comb = Label(f_painel, text="Valor do combustivel (R$):", font=('Ivy 10 bold'), bg=co0, fg=co1)
l_valor_comb.place(x=10, y=100)
e_valor_comb= Entry(f_painel, width=15, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_valor_comb.place(x=180, y=100)

l_calculo = Label(f_painel, text="Valor de consumo (R$):", font=('Ivy 10 bold'), bg=co0, fg=co1)
l_calculo.place(x=10, y=130)
e_calculo= Label(f_painel, text="", font=('Ivy 10 bold'), bg=co0, fg=co1)
e_calculo.place(x=160, y=130)

l_total_combustivel = Label(f_painel, text="Valor Total gasto Comb. (R$):", font=('Ivy 10 bold'), bg=co0, fg=co1)
l_total_combustivel.place(x=10, y=160)
e_total_combustivel= Label(f_painel, text="", font=('Ivy 10 bold'), bg=co0, fg=co1)
e_total_combustivel.place(x=200, y=160)

l_total_de_lucro = Label(f_painel, text="Total do Lucro (R$):", font=('Ivy 10 bold'), bg=co0, fg=co1)
l_total_de_lucro.place(x=10, y=190)
e_total_de_lucro= Label(f_painel, text="0", font=('Ivy 10 bold'), bg=co0, fg=co1)
e_total_de_lucro.place(x=160, y=190)

#**********************CRIANDO ENTRYS********************************
# Botoes Cabeçalho
bt_adicionar = Button(f_botoes, command=None, text="Adicionar", bd=3, bg=co0, fg=co1, font=('verdana', 9, 'bold'))
bt_adicionar.grid(row=0, column=1)

bt_atualizar = Button(f_botoes, command=None, text="Atualizar", bd=3, bg=co0, fg=co1, font=('verdana', 9, 'bold'))
bt_atualizar.grid(row=0, column=2)

bt_deletar = Button(f_botoes, command=None, text="Deletar", bd=3, bg=co0, fg=co1, font=('verdana', 9, 'bold'))
bt_deletar.grid(row=0, column=3)




#Tabela Alunos
def mostrar_lucro():
    
        app_nome = Label(f_tabela, text="Registros de Rotas", height=1, pady=0, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")  # Agora correto
        
        #CREATING A TREEVIEW WITH DUAL SCROLLBARS
        list_header = ['id', 'Data', 'Valor de Rota', 'Km Rodado', 'Calculo', 'valor Combustivel', 'Total Combustivel', 'Total']
        df_list = ver_lucro()
        
        global tree_lucro
        
        tree_lucro = ttk.Treeview(f_tabela, selectmode="extended", columns=list_header, show="headings")
        
        #VERTICAL SCROLLBAR
        vsb = ttk.Scrollbar(f_tabela, orient="vertical", command=tree_lucro.yview)
        #HORIZONTAL SCROLLBAR
        hsb = ttk.Scrollbar(f_tabela, orient="horizontal", command=tree_lucro.yview)
        
        tree_lucro.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_lucro.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        f_tabela.grid_rowconfigure(0,weight=12)
        
        hd=["center","center","center","center","center","center","center","center","center"]  
        h = [40, 100, 100, 130, 50, 160, 160, 100, 100]
        n=0
        
        for col in list_header:
            tree_lucro.heading(col, text=col.title(), anchor=NW)
            #ADJUST THE COLUMN'S WIDTH TO THE HEADER STRING
            tree_lucro.column(col, width=h[n], anchor=hd[n])
            
            n+=1
            
            for item in df_list:
                tree_lucro.insert("", "end", values=item)
mostrar_lucro()



root.mainloop()