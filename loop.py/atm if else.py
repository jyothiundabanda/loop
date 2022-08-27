from builtins import input


balance=50000
print("welcome to canara bank")
print("please insert your card")
print("please select your language")
language=input("enter the language=")
if language=="english":
    password=int(input("enter the password="))
    if password==1234:
        print("1=withdrawl")
        print("2=balance enquiry")
        print("3=pin generation")
        print("4=deposit")
        print("5=exit")
        Transaction=int(input("enter the Transaction  :"))
        if Transaction==1:
            withdrawal=int(input("enter the withdrawal="))
            if withdrawal<=balance:
                print("collect your cash",withdrawal)
                print("remaining balance",balance-withdrawal)
            else:
                print("please enter correct values") 

        if Transaction==2:
            balance_enquiry=input("savings/current=")
            if balance_enquiry=="saving":
                print("your balance",balance)
            else:
                print("enter correct values") 
        if Transaction==3:
            if password==password:
                pin_generation=int(input("enter the new pin  :"))
                print("new pin generated successfully",pin_generation)  
            else:
                print("not correct") 
        if Transaction==4:
            deposit=int(input("enter the deposit money:")) 
            if deposit>=10:
                print("total money is:",balance+deposit)  
                print("money is deposit successfully")  
            else:
                print("no deposit")  
        if Transaction==5:
            exit=input("do you want to exit=")  
            if exit=="yes":
                print("thank you for visiting")
            else:
                print("choose your transaction")  
    else:
        print("enter correct password")                  
else:
    print("language doesnt exit")                                   
