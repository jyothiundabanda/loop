from builtins import input


n=int(input("no"))
i=65
while i<=n:
    j=65
    while j<=i:
        print(chr(j),end="")
        j=j+1
    i=i+1
    print()

# n=int(input("no"))
# i=65
# while i<n:
#     j=i
#     while j>=65:
#         print(chr(i),end="")
#         j=j-1
#     i=i+1
#     print()
