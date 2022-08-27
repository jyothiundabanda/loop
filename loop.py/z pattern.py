i=1
r=5
c=5
while i<=r:
    j=1
    while j<=c:
        if i==1 or i==5 or i==2 and j==4 or i==3 and j==3 or i==4 and j==2  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()