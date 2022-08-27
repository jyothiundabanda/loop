from builtins import input


age=int(input("nage"))
dose=int(input("dose"))
if age>=18:
    if dose==1:
        print("go for second dose")
    elif dose==2:
        print("thank you")
    else:
        print("go for 1st dose")
else:
    print("not eligibil")