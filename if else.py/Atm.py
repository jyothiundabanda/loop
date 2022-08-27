# s==1:
#             cashwithdraw=int(input("enter the withdraw"))
#             if cashwithdraw<=balance:
#                 print("collect your amount")
#                 print("remaining balance:",balance-cashwithdraw)
#             else:
#                 print("please enter correct amount")
#         elif trans==2:
#             balance=input("savings/current")
#             if balaprint=("wellcome to canara bank")
# print=("please insert your card")
# print=("select your language")
# balance=200000
# language=input("enter the language")
# if language=="english":
#     password=int(input("enter the password:"))
#     if password==7799:
#         print("1.cashwithdraw")
#         print("2.balance")
#         print("3.pingenaration")
#         print("4.deposite")
#         print("5.exit")
#         trans=int(input("choose the trans"))
#         if trannce=="savings":
#                 print("your balance",balance)
#             else:
#                 print("enter correct number")
#         elif trans==3:
#             pingenaration=int(input("enter the pin generation"))
#             if pingenaration==8003:
#                 print("new pin generate succefully")
#             else:
#                 print("enter current number")
#         elif trans==4:
#             deposite=int(input("enter the deposite"))
#             if deposite>=10:
#                 print("money deposite successfully")
#             else:
#                 print("no deposite")
#         elif trans==5:
#             exit=input("do you want to exit")
#             if exit=="yes":
#                 print("thank you for visiting")
#         else:
#             print("choose your valid transaction")
#     else:
#         print("please correct password")
# else:
#     print("language does not exit")




from builtins import input


total_amount=int(input("enter the total_amount:"))
print("WELCOME TO SBI")
select_language=input("enter the language:")
if select_language=="english" or select_language=="telugu":
    num=int(input("enter the 2 digit number:"))
    if num>=10 and num<=99:
        print("1.withdrawl")
        print("2.balance enquiry")
        print("3.deposit")
        a=int(input("please choose the transaction:"))
        if a==1:
            w=int(input("enter the withdrawl amount:"))
            if w<total_amount and w%100==0:
                pin=int(input("enter the pin:"))
                if pin>=1000 and pin<=9999:
                    print("please collect your cash")
                else:
                    print("enter valid pin")
            elif a==2:
                print("your available balance is:",total_amount)
            elif a==3:
                deposit=int(input("deposit money:"))
                if deposit>=10:
                    print("cash is added")
                    print("available amount is:", total_amount+add_cash)
                else:
                    print("enter valid cash")
    else:
        print("please enter correct 2 digit number")
else:
    print("please select proper language")