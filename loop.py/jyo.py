from builtins import input
from operator import iadd


# n=int(input("no"))
# i=1
# while i<=n:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j)
#         j=j+1
#     i=i+1


# n=int(input("no"))
# i=1
# while i<=n:
#     k=1
#     while k<=n-i:
#         print(" ",end="")
#         k=k+1
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the no"))
# i=1
# while i<=n:
#     k=1
#     while k<=n-i:
#         print("",end=" ")
#         k=k+1
#     j=i
#     while j>=1:
#         print(j,end="")
#         j=j-1
#     m=2
#     while m<=i:
#         print(m,end="")
#         m=m+1
#     i=i+1
#     print()

n=int(input("no"))
i=1
while i<=n:
    j=5
    while j>=i:
        print(j,end="")
        j-=1
    i=i+1
    print()