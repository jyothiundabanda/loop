from builtins import input


n=int(input("no"))
a=0
c=1
s=0
while s<=n:
    print(s)
    a=c
    c=s
    s=a+c