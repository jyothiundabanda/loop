from builtins import input


a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a<c:
    print(a,"is middle")
elif a<b and a>c:
    print(a,"is middle")
elif b>a and b<c:
    print(b,"is middle")
elif b<a and b>c:
    print(b,"is a middle")
elif c>a and c<b:
    print(c,"is a middle")
elif c<a and c>b:
    print(c,"is a middle")
else:
    print("ntg")