from builtins import input


n=int(input("no"))
i=1
while i<=n:
    j=1
    while j<=n:
        print(j,end="")
        j=j+1
    i=i+1
    print()