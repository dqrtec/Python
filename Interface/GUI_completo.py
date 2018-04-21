import tkinter as tk

janela = tk.Tk()

janela.title("Daniel")
janela["bg"] = "red"

lb = tk.Label(janela , text="Fala galera")
lb.place(x=100 , y=100)

lb2 = tk.Label(janela , text="Fala galera")
lb2.pack(fill=x,expand=1)#fill sempre irá ocupar todo o (x,y,BOTH)
#expand divide em partes proporcionais

lb3 = tk.Label(janela , text="Fala galera")
lb3.grid(row=1 , column = 1)

janela.geometry("300x300+100+100")

janela.mainloop()
