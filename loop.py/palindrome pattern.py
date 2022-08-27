from builtins import input
from tkinter import N


n=int(input("enter the no"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print("",end=" ")
        k=k+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    m=2
    while m<=i:
        print(m,end="")
        m=m+1
    i=i+1
    print()



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

# n=int(input("enter the no"))
# i=1
# while i<=n:
#     k=1
#     while k<=i:
#         print(k,end="")
#         k=k+1
#     j=i-1
#     while j>=1:
#         print(j,end="")
#         j=j-1
#     i=i+1
#     print()

# n=int(input("the"))
# for i in range(1,n+1):
#     print(((10**i-1)//9)**2)
# n=int(input("ghj"))
# i=1
# while i<=n:
#     print(((10**i-1)//9)**2)
#     i=i+1

# a="manpreet"
# b=7.0
# c=1
# d=int(b)
# e=str(d+c)
# print("''",a+e,"''")

# n=int(input("no"))
# i=1
# while i<=3:
#     j=1
#     while j<=3-i:
#         print(" ",end="")
#         j=j+1
#     r=n
#     while r<=(n*2)-i:
#         print("*",end="")
#         r=r+1
#     i=i+1
#     print()

# n=int(input("no"))
# i=1
# k=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(k,end="")
#         j=j+1
#         k=k+1
#     i=i+1
#     print()

# n=int(input("no"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i*2,end=" ")
#         j=j+1
#     i+=1
#     print()