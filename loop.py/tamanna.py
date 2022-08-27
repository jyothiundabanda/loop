from builtins import input


n=int(input("no"))
i=1
while n>0:
    j=1
    while j<i:
        print(" ",end="")
        j=j+1
    b=1
    while b<=n:
        print("*",end=" ")
        b=b+1
    i=i+1
    print()
    n=n-1
    