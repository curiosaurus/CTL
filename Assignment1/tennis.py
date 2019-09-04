def disp(serp,plp):
    print("--------------------------points are------------------------- \nServer Points "+str(serp)+"-"+str(plp)+"Player Points ")
serp=0
plp=0
state="running"
print("-------------------------------------Game starts-------------------------")
disp(serp,plp)
while(state=="running"):
        setw=input("Who won the set ")
        #setresult(setw)
        if(setw=="s" or setw=="S"):
            serp+=15
            if (serp==45):
                serp-=5
        elif(setw=="p" or setw=="P"):
            plp+=15
            if (plp==45):
                plp-=5
        else:
            print("invalid input")
        disp(serp,plp)
        if(serp==plp and serp==40):
            state="tie"
            print("GAME TIED")
            break
        if(serp>45):
            print("SERVER WINS")
            break
        if(plp>45):
            print("PLAYER WINS")
            break
while(state=="tie"):
        setw=input("Who won the set ")
        if(setw=="s" or setw=="S"):
            serp+=1
        elif(setw=="p" or setw=="P"):
            plp+=1
        else:
            print("invalid input")
        if(plp==serp):
            plp=40
            serp=40
        disp(serp,plp)
        if(serp==42):
            print("SERVER WINS")
            break
        if(plp==42):
            print("PLAYER WINS")
            break