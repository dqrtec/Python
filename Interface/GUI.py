from tkinter import * #importar o framework da interface grafica
import tkinter #importar o framework da interface grafica

############   CRIANDO EVENTO 1
##class Application:
##    def __init__(self , master = None):
##        self.widget1 = Frame(master)
##        self.widget1.pack()
##        self.msg = Label(self.widget1, text = "Primeiro widget")
##        self.msg["font"] = ("Verdana","10","italic","bold")
##        self.msg.pack()
##
##        self.sair = Button(self.widget1)
##        self.sair["text"] = "Sair"
##        self.sair["font"] = ("Calibri","40")
##        self.sair["width"] = 5
##        self.sair.bind("<Button-1>",self.mudarTexto)
##        self.sair.pack(side = RIGHT)
##
##    def mudarTexto(self , event):
##        if self.msg["text"] == "Primeiro widget":
##            self.msg["text"] = "O botão recebeu um clique"
##        else:
##            self.msg["text"] = "Primeiro widget"
############################

############   CRIANDO EVENTO 2
##class Application:
##    def __init__(self , master = None):
##        self.widget1 = Frame(master)
##        self.widget1.pack()
##        self.msg = Label(self.widget1, text = "Primeiro widget")
##        self.msg["font"] = ("Verdana","10","italic","bold")
##        self.msg.pack()
##
##        self.sair = Button(self.widget1)
##        self.sair["text"] = "Sair"
##        self.sair["font"] = ("Calibri","40")
##        self.sair["width"] = 5
##        self.sair["command"] = self.mudarTexto
##        self.sair.pack()
##
##    def mudarTexto(self):
##        if self.msg["text"] == "Primeiro widget":
##            self.msg["text"] = "O botão recebeu um clique"
##        else:
##            self.msg["text"] = "Primeiro widget"
############################

class Application:
      def __init__(self, master=None):
          self.fontePadrao = ("Arial","10")
          self.primeiroContainer = Frame(master)
          self.primeiroContainer["pady"] = 10
          self.primeiroContainer.pack()

          self.segundoContainer = Frame(master)
          self.segundoContainer["padx"] = 20
          self.segundoContainer.pack()

          self.terceiroContainer = Frame(master)
          self.terceiroContainer["padx"] = 20
          self.terceiroContainer.pack()

          self.quartoContainer = Frame(master)
          self.quartoContainer["pady"] = 20
          self.quartoContainer.pack()

          self.titulo = Label(self.primeiroContainer , text="Dados do usuário")
          self.titulo["font"] = ("Arial","10","bold")
          self.titulo.pack()

          self.nomeLabel = Label(self.segundoContainer , text = "Nome",font = self.fontePadrao)
          self.nomeLabel.pack(side = LEFT)
          

          self.nome = Entry(self.segundoContainer)
          self.nome["width"] = 30
          self.nome["font"] = self.fontePadrao
          self.nome.pack(side = LEFT)

          self.senhaLabel = Label(self.terceiroContainer , text ="Senha" , font = self.fontePadrao)
          self.senhaLabel.pack(side = LEFT)

          self.senha = Entry(self.terceiroContainer)
          self.senha["width"] = 30
          self.senha["font"] = self.fontePadrao
          self.senha["show"] = "*"
          self.senha.pack(side = LEFT)

          self.autenticar = Button(self.quartoContainer)
          self.autenticar["text"] = "Autenticar"
          self.autenticar["font"] = ("Calibri","8")
          self.autenticar["width"] = 12
          self.autenticar["command"] = self.verificaSenha
          self.autenticar.pack()

          self.mensagem = Label(self.quartoContainer , text="" , font = self.fontePadrao)
          self.mensagem.pack()

    

      #Método verificar senha
      def verificaSenha(self):
          usuario = self.nome.get()
          senha = self.senha.get()
          if usuario == "daniel" and senha=="123":
              self.mensagem["text"] = "Autenticado"
          else:
              self.mensagem["text"] = "INTRUSO!!!!"
              
          

          
          



          
          
root = Tk() #Cria a tela
Application(root)
root.mainloop()

