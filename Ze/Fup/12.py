array=[1,2,3,9,8,7]

def maxi(n , maior):
    if n >0:
        if array[n-1] > maior:
            maior = array[n-1]
        return maxi(n-1,maior)
    else:
        return maior





print(maxi(len(array) , array[0]))
