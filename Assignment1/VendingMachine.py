moneyr=0
while(moneyr<125):
    print("---------------------Total Money received "+str(moneyr)+" rs---------------------\n ------------------------------input atleast "+str(125-moneyr)+" rs-------------------------------------\n * We only take 25Rs and 100Rs coins*")
    mr=int(input("put money :"))
    if(mr==25 or mr==100):
        moneyr+=mr #moneyr=moneyr+mr
    else:
        print("-------------------------------------------------------------------------\nInvalid input currency please recollect the cash")
print("Here is your soda of Rs125 \n You have deposited:"+str(moneyr)+" rs \nrecollect the change:"+str(moneyr-125)+" rs")