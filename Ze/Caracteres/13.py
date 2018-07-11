from random import randint
captcha=[]
def sorte(a):
    s=randint(0,100)
    if s>50:
        captcha.insert(0,chr(a))
    else:
        captcha.append(chr(a))
        
times=0

while times<2:
    times+=1
    maius = randint(65,90)
    sorte(maius)
    minus = randint(97,122)
    sorte(minus)
    num = randint(48,57)
    sorte(num)
print(captcha)
