from builtins import input


i=int(input("no"))
j=int(input("no"))
c=0
s=0
while i<j:
    if i%2==0:
        c=c+1
    else:
        s=s+i
    i=i+1
print(c)
print(s)