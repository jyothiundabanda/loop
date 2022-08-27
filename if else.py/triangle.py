from builtins import input


a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
if a+b+c==180:
    print("valid trangle")
else:
    print("invalid")



a=int(input("enter the equilateral"))
b=int(input("enter the isosceles"))
c=int(input("enter the scalenes"))
if a==b==c:
    print("equilateral traingle")
elif b==c or a==b or a==c:
    print("iscsceles traingle")
else:
    print("scalenes")
