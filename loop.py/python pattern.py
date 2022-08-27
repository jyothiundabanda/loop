from builtins import input
n=input("*")
len=len(n)
r=0
while r<=len-1:
    c=0
    while c<=r:
        print(n[c],end=" ")
        c=c+1
    r=r+1
    print()