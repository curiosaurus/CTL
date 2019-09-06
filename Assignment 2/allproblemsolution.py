import sys
allowed_chars = set('ab')
ch=0
while(ch!=6):
    print("--------------------------------------------------------------------------------------------------\n1. Task 1\n2. Task 2\n3. Task 3\n4. Task 4 \n5. Task 5 \n6.Exit\n-----------------------------------------------------------------------------------------------")
    ch=int(input("Enter the Choice"))
    if(ch==1):
        st=input("Enter the String of equal no. of As followed By Equal no. of Bs:  ")
        counta=sum(map(lambda x : 1 if 'a' in x else 0, st))
        countb=sum(map(lambda x : 1 if 'b' in x else 0, st))
        if (counta == countb) and (counta > 0 ) and (len(st)==counta*2): 
            for i in st[0:(counta):1]:   
                if (i !='a'): 
                    print("String is wrong")
            print("string is right")
        else: print("String is wrong")
    elif(ch==2):
        string=input("Enter a String of As and Bs where first and last symbol are same: ")
        if set(string).issubset(allowed_chars):
            if(string[0]==string[-1]): print("Condition satisfied")
            else:
                print("invalid String")
        else: print("Invalid String")
    elif(ch==3):
        st=input("Enter the String of As And Bs where no. of As divisible by 2 : ")
        if set(st).issubset(allowed_chars):
            counta=sum(map(lambda x : 1 if 'a' in x else 0, st))
            if (counta%2==0):
                print("Valid String")
            else:
                print("Invalid String")
        else: print("Invalid String")
    elif(ch==5):
        st=input("Enter the String of As And Bs where no. of As divisible by 4 and Bs not divisble by 3: ")
        if set(st).issubset(allowed_chars):
            counta=sum(map(lambda x : 1 if 'a' in x else 0, st))
            countb=sum(map(lambda x : 1 if 'b' in x else 0, st))
            if (counta%4==0 and countb%3!=0):
                print("Valid String")
            else:
                print("Invalid String")
        else: print("Invalid String")
    elif(ch==4):
        st=int(input("Enter a binary String whose valuse is divisible by 5 : "),2)
        print(st)
        if st%5==0:
            print("Valid string")
        else:
            print("Invalid String")
    elif(ch==6):
        exit()
    else:
        print("Invalid input")