#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


# In[30]:


cliente1 = Cliente("Daniel", "837489")


# In[31]:


class Conta:
    numero = 1
    def __init__(self, dono):
        self.n_conta = self.numero
        self.numero = self.numero + 1
        self.dono = dono
        self.saldo = 0
    def depositar(self, acrescimo):
        self.saldo = acrescimo
    def saque(self,valor):
        if(valor<=self.saldo):
            print("texto grande")
        else:
            print("Saldo insuficiente!")
    def extrato(self):
        pass
    
    
class Especial(Conta):
    def __init__(self,dono,limite):
        super().__init__(dono)
        self.limite = limite
    def saque(self, valor):
        if (self.saldo + self.limite) >= valor:
            print("""Extrato CC No. {0}
        \t DEPOSITO \t {1:0.2f}
        \t Saque \t\t {2:0.2f}\n
        \t Saldo \t\t {3:0.2f}
        \n
        \t Limite \t {4:0.2f}\n\n
        Disponivel \t\t {5:0.2f}
        """.format(self.n_conta, self.saldo, valor,(self.saldo-valor) ,self.limite, (self.limite+self.saldo-valor)))
            self.saldo = self.saldo-valor
            if valor > self.saldo:
                self.limite = self.limite + self.saldo - valor
        else:
            print("Saldo insuficiente!")
    def extrato(self):
        print("""Extrato CC No. {0}
        \t DEPOSITO \t {1:0.2f}
        \t Saldo \t\t {2:0.2f}
        \n
        \t Limite \t {3:0.2f}\n\n
        Disponivel \t\t {4:0.2f}
        """.format(self.n_conta, self.saldo, self.saldo, self.limite, (self.saldo+self.limite)))


# In[32]:


conta2 = Especial(cliente1,1000)
conta2.depositar(5000.00)
conta2.extrato()


# In[33]:


conta2.saque(8000)


# In[34]:


conta2.saque(7000)


# In[35]:


conta2.saque(6000)

