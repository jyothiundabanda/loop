from builtins import input


n=int(input("no"))
a=0
i=1
while n>i:
    r=n%10
    a=a+(r*10)
    i=i*2
    n=int(n/10)
print(a)