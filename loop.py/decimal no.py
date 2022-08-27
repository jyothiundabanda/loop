from builtins import input


n=int(input("no"))
a=0
i=1
while n>0:
    r=n%10
    a=a+(r*i)
    i=i*2
    n=n//10
print(a)
