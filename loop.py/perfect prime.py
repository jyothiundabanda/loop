from builtins import input

# n=int(input("no"))
# i=1
# s=0
# while i<n:
#     if n%i==0:
#         s=s+i
#     i=i+1
# if s==n:
#     print("perfect no")
# else:
#     print("not")


i=0
while i<=6:
    j=0
    while j<=4:
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end=" ")
        else:
            print(end="  ")
        j=j+1
    i=i+1
    print()


# for i in range(7):
#     for j in range(6):
#         if ((j==0 or j==4) and row:
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print( )