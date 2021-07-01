#1
def counting(x):
    al=[]
    Al=[]
    for i in x:
        if i.islower():
            al.append(i)
        else:
            Al.append(i)
    a=str(len(al))
    b=str(len(Al))
    print('Сумма заглавных букв - ',b  )
    print('Сумма строчных букв - ',a)
    
    #2
    def prost(a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
    else:
        print("Число нe простoe")
        
        #3
        def povtor(a):
    pl=[]
    for e in a:
        if e not in pl:
            pl.append(e)
        ps=''.join(pl)
    print(ps)
