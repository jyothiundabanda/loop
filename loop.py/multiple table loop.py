# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j)
#         j=j+1
#     i+=1
#     print()



# single MULTIPLE

# i=1
# j=3
# while i<=10:
#     print(j,"*",i,"=",j*i)
#     i=i+1

from builtins import input


n=int(input("yu"))
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2==0:
            print(j,end=" ")
        else:
            print("*",end=" ")
        j=j+1
    i=i+1
    print()
