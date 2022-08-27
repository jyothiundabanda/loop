from builtins import input


n=int(input("no"))
i=5
while i>=0:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i-1
    print()

# i=1
# while i<=100:
#     if i%7==0:
#         print(i)
#     i=i+1           
