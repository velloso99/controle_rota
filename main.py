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

f_botoes = Frame(root, width=850, height=65, bg=co0)
f_botoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

#**********************CRIANDO LABEL********************************


l_titulo = Label(f_titulo, text="Cadastro de rotas", font=('Ivy 20 bold'), bg=co0, fg=co1)
l_titulo.place(x=430, y=23, anchor=CENTER)


# Botoes Cabeçalho
app_img_add = Image.open('img/save.png')
app_img_add = app_img_add.resize((18,18))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(f_botoes,command=None, image=app_img_add, text="Salvar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_add.grid(row=0, column=1)

app_img_update = Image.open('img/update.png')
app_img_update = app_img_update.resize((18,18))
app_img_update = ImageTk.PhotoImage(app_img_update)
app_update = Button(f_botoes,command=None, image=app_img_update, text="Atualizar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_update.grid(row=0, column=2)

app_img_delete = Image.open('img/delete.png')
app_img_delete = app_img_delete.resize((18,18))
app_img_delete = ImageTk.PhotoImage(app_img_delete)
app_delete = Button(f_botoes,command=None, image=app_img_delete, text="Deletar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_delete.grid(row=0, column=3)



root.mainloop()