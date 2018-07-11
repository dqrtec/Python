array=[1,2,3,4]

def soma(i):
    if i>0:
        return array[i-1] + soma(i-1)
    else:
        return 0 

print(soma(len(array)))
    
