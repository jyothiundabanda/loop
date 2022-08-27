i=0
while i<=6:
    j=0
    while j<=4:
        if  ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end=" ")
        else:
            print(end="  ")
        j=j+1
    i=i+1
    print()

