for i in range(6):
    for j in range(7):
        if i==0 and j%3!=0 or i==1 and j%3==0 or i-j==2 or i+j==8:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# i=1
# r=5
# c=4
# while i<=r:
#     j=1
#     while j<=c:
#         if j==1 or i==5 or i==3 or i==1 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j=j+1
#     i=i+1
#     print()[  2q  2Q  ]