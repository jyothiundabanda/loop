from builtins import input


n=int(input("no"))
i=1
while i<=n:
    j=1
    while j>=i:
        print(str(j)*i,end="")
        j=j-1
    i=i+2
    print()