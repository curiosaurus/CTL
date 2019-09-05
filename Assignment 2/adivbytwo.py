st=input("Enter the String of As And Bs with no. of As divisible by 2 : ")
counta=sum(map(lambda x : 1 if 'a' in x else 0, st))
if (counta%2==0):
    print("Valid String")
else:
    print("Invalid String")