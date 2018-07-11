'''
1. Cadastrar tombo;
2. Cadastrar obra; 
'''

obra=[
{"tombo":1,"exemplar":2,"data_compra":"1995"},
{"tombo":2,"exemplar":1,"data_compra":"1991"},
{"tombo":3,"exemplar":3,"data_compra":"1992"},
{"tombo":4,"exemplar":2,"data_compra":"1993"},
{"tombo":5,"exemplar":1,"data_compra":"1994"},
{"tombo":6,"exemplar":3,"data_compra":"1995"},
{"tombo":7,"exemplar":2,"data_compra":"1991"},
{"tombo":8,"exemplar":1,"data_compra":"1992"},
{"tombo":9,"exemplar":3,"data_compra":"1993"},
{"tombo":10,"exemplar":2,"data_compra":"1995"},
{"tombo":11,"exemplar":1,"data_compra":"1991"},
{"tombo":12,"exemplar":3,"data_compra":"1992"},
{"tombo":13,"exemplar":2,"data_compra":"1993"},
{"tombo":14,"exemplar":1,"data_compra":"1994"},
{"tombo":15,"exemplar":3,"data_compra":"1995"},
{"tombo":16,"exemplar":2,"data_compra":"1991"},
{"tombo":17,"exemplar":1,"data_compra":"1992"},
{"tombo":18,"exemplar":3,"data_compra":"1993"},
{"tombo":19,"exemplar":2,"data_compra":"1994"},
{"tombo":20,"exemplar":1,"data_compra":"1995"},
]
tombo=[
{"tombo":1,"nome":"ilha das rosas1","autor":"mauricio","editora":"moderna1","ano":1981},
{"tombo":2,"nome":"ilha das rosas2","autor":"mauricio","editora":"moderna1","ano":1982},
{"tombo":3,"nome":"ilha das rosas3","autor":"mauricio","editora":"moderna1","ano":1983},
{"tombo":4,"nome":"ilha das rosas4","autor":"mauricio","editora":"moderna1","ano":1984},
{"tombo":5,"nome":"ilha das rosas5","autor":"mauricio","editora":"moderna2","ano":1985},
{"tombo":6,"nome":"ilha das rosas6","autor":"mauricio","editora":"moderna2","ano":1986},
{"tombo":7,"nome":"ilha das rosas7","autor":"mauricio","editora":"moderna2","ano":1987},
{"tombo":8,"nome":"ilha das rosas8","autor":"mauricio","editora":"moderna2","ano":1988},
{"tombo":9,"nome":"ilha das rosas9","autor":"mauricio","editora":"moderna1","ano":1989},
{"tombo":10,"nome":"ilha das rosas0","autor":"mauricio","editora":"moderna1","ano":1980},
{"tombo":11,"nome":"ilha das rosasa","autor":"mauricio","editora":"moderna0","ano":1980},
{"tombo":12,"nome":"ilha das rosass","autor":"mauricio","editora":"moderna9","ano":1980},
{"tombo":13,"nome":"ilha das rosasd","autor":"mauricio","editora":"moderna8","ano":1981},
{"tombo":14,"nome":"ilha das rosasf","autor":"mauricio","editora":"moderna7","ano":1980},
{"tombo":15,"nome":"ilha das rosasg","autor":"mauricio","editora":"moderna6","ano":1981},
{"tombo":16,"nome":"ilha das rosash","autor":"mauricio","editora":"moderna5","ano":1980},
{"tombo":17,"nome":"ilha das rosasj","autor":"mauricio","editora":"moderna4","ano":1980},
{"tombo":18,"nome":"ilha das rosask","autor":"mauricio","editora":"moderna3","ano":1983},
{"tombo":19,"nome":"ilha das rosasl","autor":"mauricio","editora":"moderna2","ano":1980},
{"tombo":20,"nome":"ilha das rosasq","autor":"mauricio","editora":"moderna1","ano":1985}
]
menu=True
while menu:
    print("\nescolha uma das opções\n1-cadastrar tombo\n2-cadastrar obra\n3-mostrar obras por ano\n4-mostrar obras por autor\n5-mostrar obra por editora\n6encerrar programa")
    m=int(input(">>"))

    if m==6:
        menu=False
    elif m==4:
        print("")
        autor1=input("Nome do autor ")
        for i in range(len(tombo)):
            if  tombo[i]["autor"]== autor1 :
                print(tombo[i]["nome"])
    elif m==5:
        print("")
        editora=input("Nome da editora ")
        for i in range(len(tombo)):
            if  tombo[i]["editora"]== editora :
                print(tombo[i]["nome"])
    elif m==3:
        print("")
        ano=int(input("Digite o ano "))
        for i in range(len(tombo)):
            if  tombo[i]["ano"]== ano :
                print(tombo[i]["nome"])
    
        
            


    
