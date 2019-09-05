st=input("Enter the String :  ")
counta=sum(map(lambda x : 1 if 'a' in x else 0, st))
countb=sum(map(lambda x : 1 if 'b' in x else 0, st))
if (counta == countb) and (counta > 0 ) and (len(st)==counta*2): 
    for i in st[0:(counta):1]: 
        if (i !='a'): 
            print("String is wrong")
            exit()
    print("string is right")
else: print("String is wrong")