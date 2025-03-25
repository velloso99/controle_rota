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



#**********************CRIANDO LABEL********************************


l_titulo = Label(f_titulo, text="Cadastro de rotas", font=('Ivy 20 bold'), bg=co0, fg=co1)
l_titulo.place(x=430, y=23, anchor=CENTER)


l_id = Label(f_painel, text="id:", font=('Ivy 10 bold'), bg=co0, fg=co1)
l_id.place(x=10, y=10)
e_id= Entry(f_painel, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_id.place(x=40, y=10)


d_data_nascimento = DateEntry(f_painel, width=18, background='darkblue', foreground='white', borderwidth=2, year=2023 )
d_data_nascimento.place(x=10, y=40)  

#**********************CRIANDO ENTRYS********************************
# Botoes Cabeçalho
app_img_add = Image.open('img/save.png')
app_img_add = app_img_add.resize((18,18))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(f_botoes,command=None, image=app_img_add, text="Salvar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co0, fg=co1)
app_add.grid(row=0, column=1)

app_img_update = Image.open('img/update.png')
app_img_update = app_img_update.resize((18,18))
app_img_update = ImageTk.PhotoImage(app_img_update)
app_update = Button(f_botoes,command=None, image=app_img_update, text="Atualizar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co0, fg=co1)
app_update.grid(row=0, column=2)

app_img_delete = Image.open('img/delete.png')
app_img_delete = app_img_delete.resize((18,18))
app_img_delete = ImageTk.PhotoImage(app_img_delete)
app_delete = Button(f_botoes,command=None, image=app_img_delete, text="Deletar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co0, fg=co1)
app_delete.grid(row=0, column=3)




#Tabela Alunos
def mostrar_lucro():
    
        app_nome = Label(f_tabela, text="Registros de Rotas", height=1, pady=0, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")  # Agora correto
        
        #CREATING A TREEVIEW WITH DUAL SCROLLBARS
        list_header = ['id', 'Data', 'Valor de Rota', 'Km Rodado', 'Calculo', 'valor Combustivel', 'Total Combustivel', 'Total']
        df_list =ver_lucro()
        
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