from builtins import input


n=int(input("no"))
a=0
b=1
c=0
while c<=n:
    print(c)
    a=b
    b=c
    c=a+b

