i=1
r=5
c=3
while i<=r:
    j=1
    while j<=c:
        if j==1 or i==1 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()