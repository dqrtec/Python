from tkinter import *

tela = Tk()#tela

############################    LISTA
##scrollbar = Scrollbar(tela) #cria a barra lateral
##scrollbar.pack(side=RIGHT, fill=Y)#tamanho da barra lateral
##
##mylist = Listbox(tela, yscrollcommand = scrollbar.set )#cria uma lista
##mylist.pack( side = LEFT, fill = BOTH )
##scrollbar.config( command = mylist.yview )#linka a lista com a barra

############################    SCROLLBAR SIMPLIFICADO
##from tkinter.scrolledtext import *
##tudo = ScrolledText(tela).pack()

############################    SELECIONAR COR
##from tkinter.colorchooser import *
##def getColor():
##    color = askcolor() 
##    print(color)
##Button(text='Select Color', command=getColor).pack()

############################    ALARME 1
##class Alarm(Frame):
##    def repeater(self):                          
##        self.bell()   #som                           
##        self.stopper.flash() #pisca
##        self.after(self.msecs, self.repeater)    
##    def __init__(self, msecs=1000):              
##        Frame.__init__(self)
##        self.msecs = msecs
##        self.pack()
##        stopper = Button(self, text='Stop the beeps!', command=self.quit)
##        stopper.pack()
##        stopper.config(bg='red', fg='white', bd=2) 
##        self.stopper = stopper
##        self.repeater()   
##Alarm(msecs=1).mainloop()

############################    ALARME 2
##class Alarm(Frame):                             
##    def repeater(self):
##        self.bell()                              
##        if self.shown:
##            self.stopper.pack_forget()           
##        else:                                    
##            self.stopper.pack()
##        self.shown = not self.shown              
##        self.after(self.msecs, self.repeater)    
##    def __init__(self, msecs=1000):              
##        self.shown = 0
##        Frame.__init__(self)
##        self.msecs = msecs
##        self.pack()
##        stopper = Button(self, text='Stop the beeps!', command=self.quit)
##        stopper.pack()
##        self.stopper = stopper
##        self.repeater()
## Alarm(msecs=500).mainloop()

##########################    ALARME 3
##class Alarm(Frame):
##    def repeater(self):                           
##        self.bell()                               
##        if self.master.state() == 'normal':       
##            self.master.withdraw()                
##        else:                                     
##            self.master.deiconify()               
##            self.master.lift()                    
##        self.after(self.msecs, self.repeater)     
##    def __init__(self, msecs=1000):              
##        Frame.__init__(self)
##        self.msecs = msecs
##        self.pack()
##        stopper = Button(self, text='Stop the beeps!', command=self.quit)
##        stopper.pack()
##        self.stopper = stopper
##        self.repeater()
##Alarm().mainloop()


####################################    MENU
##menubar = Menu(tela)#instancia do menu
##filemenu = Menu(menubar , tearoff = 0)#instancia da instancia de menu #desabilita a remorção do menu
##filemenu.add_command(label="New")#,command = function
##filemenu.add_command(label="open")
##filemenu.add_command(label="Save as")
##filemenu.add_command(label="Close")
##setmenu = Menu(menubar , tearoff = 0)
##setmenu.add_checkbutton(label = "Auto",command = print(setmenu))
##menubar.add_cascade(label="checbox",menu=setmenu)
##menubar.add_cascade(label = "File",menu = filemenu) #adiciona a nova cascata no menu provisorio
##tela.config(menu = menubar)#adiciona  o menu provisorio no lugar do menu


####################################    Dialog BOX
##from tkinter import messagebox
##def msg():
##    #messagebox.showinfo(title="Titulo" , message="Esta pé a mensagem")
##    #messagebox.showwarning(title="Titulo" , message="Esta pé a mensagem")
##    case = messagebox.askyesno(title = "sair",message = "Desaeja sair?")
##    print(case)
##    if case ==True:
##        tela.destroy() 
##button = Button(tela,text="MENSAGEM",command=msg).pack()

####################################    OPEN FILE
##from tkinter import filedialog
##def mopen():
##    myopen = filedialog.askopenfile()
##button = Button(tela,text="OPEN",command=mopen).pack()


####################################    RADIO
##radio1 = Radiobutton(tela,text="op1",value = 13).pack()
##radio2 = Radiobutton(tela,text="op2",value = 2 , variable ="G_1").pack()
##radio3 = Radiobutton(tela,text="op3",value = 3 , variable ="G_1").pack()


####################################    RANGE
#spinbox1 = Spinbox(tela , from_=0,to = 10 , state = DISABLED).pack()


####################################    LIST BOX
##List1 = Listbox(tela)
##List1.insert(0,"daniel")
##List1.insert(0,"daniel2")
##List1.insert(0,"samuel")
##List1.pack()

####################################    RANGE MELHORADO
##slider_1 =  Scale(tela,orient =HORIZONTAL , length=300 , width = 50 , from_=50,to =520 , sliderlength = 50 , tickinterval = 100).pack()


####################################    CHECK BOX
##def mostra():
##    print(mvar)
##mvar = IntVar()
##chec1 = Checkbutton(tela,state = ACTIVE , onvalue = 1 , offvalue = 50,command=mostra,variable = mvar).pack()

######################################    FORMAS GEOMETRICAS
##canvas = Canvas(tela)
##canvas.create_arc(100,150,200,300,fill="blue")
##canvas.create_rectangle(50,100,150,200)
##canvas.create_oval(50,150,200,0)
##canvas.pack()

######################################    BOTAO STYLE
##widget = Button(text='Spam', padx=0, pady=0)
##widget.pack(padx=20, pady=20)
##widget.config(cursor='gumby')
##widget.config(bd=100, relief=RAISED)
##widget.config(font=('helvetica', 20, 'underline italic'))
##mainloop()

######################################    PINTURA
##class PaintBox( Frame ):
##   def __init__( self ):
##      Frame.__init__( self )
##      self.pack( expand = YES, fill = BOTH )
##      self.master.title( "title" )
##      self.master.geometry( "300x150" )
##
##      self.message = Label( self, text = "Drag the mouse to draw" )
##      self.message.pack( side = BOTTOM )
##      
##      self.myCanvas = Canvas( self )
##      self.myCanvas.pack( expand = YES, fill = BOTH )
##
##      self.myCanvas.bind( "<B3-Motion>", self.paint )
##
##   def paint( self, event ):
##      x1, y1 = ( event.x - 4 ), ( event.y - 4 )
##      x2, y2 = ( event.x + 4 ), ( event.y + 4 )
##      self.myCanvas.create_oval( x1, y1, x2, y2, fill = "red" )
##   
##PaintBox().mainloop()



######################################    BOATAO FUNCIONA COM O ENTER
##class MyApp:
##  def __init__(self, parent):
##    self.myParent = parent   
##    self.myContainer1 = Frame(parent)
##    self.myContainer1.pack()
##    self.button1 = Button(self.myContainer1, command=self.button1Click)  
##    self.button1.bind("<Return>", self.button1Click_a)   
##    self.button1.configure(text="OK", background= "green")
##    self.button1.pack(side=LEFT)
##    self.button1.focus_force()#o botao fica selecionado
##  def button1Click(self): 
##    print ("button1Click event handler" )
##    if self.button1["background"] == "green":  
##      self.button1["background"] = "yellow"
##    else:
##      self.button1["background"] = "green"
##  def button2Click(self):
##    print ("button2Click event handler" )
##    self.myParent.destroy()      
##  def button1Click_a(self, event): 
##    print ("button1Click_a event handler (a wrapper)" )
##    self.button1Click()
##  def button2Click_a(self, event): 
##    print ("button2Click_a event handler (a wrapper)" )
##    self.button2Click()    
##root = Tk()
##myapp = MyApp(root)
##root.mainloop()


######################################    CAPTURA DE CLICK
##def showPosEvent(event):
##    print ('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))
##def onLeftDrag(event):
##    print ('Got left mouse button drag:',showPosEvent(event))
##tkroot = Tk()
##labelfont = ('courier', 20, 'bold')                
##widget = Label(tkroot, text='Hello bind world')
##widget.config(bg='red', font=labelfont)            
##widget.config(height=5, width=20)                  
##widget.pack(expand=YES, fill=BOTH)
##widget.bind('<B1-Motion>', onLeftDrag)             
##widget.focus()                                     
##tkroot.title('Click Me')
##tkroot.mainloop()


##############################################    SUB BARRA DE MENU
##def notdone():  
##    showerror('Not implemented', 'Not yet available') 
##def makemenu(parent):
##    menubar = Frame(parent)                        
##    menubar.pack(side=TOP, fill=X)
##    fbutton = Menubutton(menubar, text='File', underline=0)
##    fbutton.pack(side=LEFT)
##    file = Menu(fbutton)
##    file.add_command(label='New...',  command=notdone,     underline=0)
##    file.add_command(label='Open...', command=notdone,     underline=0)
##    file.add_command(label='Quit',    command=parent.quit, underline=0)
##    fbutton.config(menu=file)
##    ebutton = Menubutton(menubar, text='Edit', underline=0)
##    ebutton.pack(side=LEFT)
##    edit = Menu(ebutton, tearoff=0)
##    edit.add_command(label='Cut',     command=notdone,     underline=0)
##    edit.add_command(label='Paste',   command=notdone,     underline=0)
##    edit.add_separator()
##    ebutton.config(menu=edit)
##    submenu = Menu(edit, tearoff=0)
##    submenu.add_command(label='Spam', command=parent.quit, underline=0)
##    submenu.add_command(label='Eggs', command=notdone,     underline=0)
##    edit.add_cascade(label='Stuff',   menu=submenu,        underline=0)
##    return menubar
##root = Tk()
##for i in range(3):
##    frm = Frame()  
##    mnu = makemenu(frm)
##    mnu.config(bd=2, relief=RAISED)
##    frm.pack(expand=YES, fill=BOTH)
##    Label(frm, bg='black', height=5, width=15).pack(expand=YES, fill=BOTH)
##Button(root, text="Bye", command=root.quit).pack()
##root.mainloop()

########################################    SUB MENU NO BOTAO
##root    = Tk()
##mbutton = Menubutton(root, text='Food')     # the pull-down stands alone
##picks   = Menu(mbutton)               
##mbutton.config(menu=picks)           
##picks.add_command(label='spam',  command=root.quit)
##picks.add_command(label='eggs',  command=root.quit)
##picks.add_command(label='bacon', command=root.quit)
##mbutton.pack()
##mbutton.config(bg='white', bd=4, relief=RAISED)
##root.mainloop()

########################################    MENU CLICAR DIREITO
##class ContextMenuTest :
##    def Cut(self) :
##        pass
##    def Copy(self) :
##        pass
##    def Paste(self) :
##        pass
##    def OnContext(self, args) :
##        contextMenu = Menu(None, tearoff=0)
##        contextMenu.add_command( label = "Cut", command = self.Cut )
##        contextMenu.add_command( label = "Copy", command = self.Copy )
##        contextMenu.add_command( label = "Paste", command = self.Paste )
##        contextMenu.tk_popup(args.x_root, args.y_root, entry="")
##    def __init__(self) :
##        self.root = Tk()
##        self.root.geometry("300x500")
##        self.root.bind("<Button-3>", self.OnContext )
##        self.root.mainloop()
##cmt = ContextMenuTest()

##########################################    SEPARADOR DE MENUS
##class MenuTest :
##    def NewFile(self) :
##        pass
##    def OpenFile(self) :
##        pass
##    def Close(self) :
##        self.root.destroy()
##    def notdone(self) :
##        pass
##    def __init__(self) :
##        self.root = Tk()
##
##        self.main_menu = Menu(self.root)
##        self.root.config( menu = self.main_menu )
##
##        fileMenu = Menu(self.main_menu)
##
##        self.main_menu.add_cascade( label="e", menu=fileMenu )
##
##        fileMenu.add_command( label="w", command=self.NewFile )
##        fileMenu.add_command( label="n", command=self.OpenFile )
##        fileMenu.add_separator() ## separa com  uma linha os itens do menu
##        fileMenu.add_command( label="t", command=self.Close )
##
##        toolMenu = Menu(self.main_menu)
##        self.main_menu.add_cascade( label="s", menu=toolMenu )
##        toolMenu.add_command( label="1", command=self.notdone )
##        submenu = Menu(toolMenu)
##        toolMenu.add_cascade( label="s", menu=submenu)
##        submenu.add_command(label="Other 1", command=self.notdone)
##        submenu.add_command(label="Other 2", command=self.notdone)
##
##        self.root.mainloop()
##
##mt = MenuTest()

################################    DUPLO CLICK
##widget.bind('<Double-1>',  onDoubleLeftClick)





mainloop()
