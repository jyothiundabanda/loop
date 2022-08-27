from builtins import input


n=int(input("no"))
i=1
while i<=5:
    r=i**n
    print(str(r)*i)
    i=i+1