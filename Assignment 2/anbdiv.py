st=input("Enter the String of As And Bs where no. of As divisible by 4 and Bs not divisble by 3: ")
counta=sum(map(lambda x : 1 if 'a' in x else 0, st))
countb=sum(map(lambda x : 1 if 'b' in x else 0, st))
if (counta%4==0 and countb%3!=0):
    print("Valid String")
else:
    print("Invalid String")