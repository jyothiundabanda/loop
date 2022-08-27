# n=int(input("no"))
# i=1
# while i<=n:
#     j=5
#     while j>=i:
#         print(i,end="")
#         j=j-1
#     i=i+1
#     print()


from builtins import input


n=int(input("no"))
i=1
while i<=n:
    j=5
    while j>=i:
        print(j,end=" ")
        j=j-1
    i=i+1
    print()