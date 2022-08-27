from builtins import input


n=int(input("no"))
i=5
while i>=n:
    j=5
    while j>=i:
        print(i,end="")
        j=j-1
    i=i-1
    print()
   