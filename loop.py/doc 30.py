from builtins import input


n=int(input("no"))
i=0
s=0
while i<n:
    s=s+i**3
    i=i+1
print(s)