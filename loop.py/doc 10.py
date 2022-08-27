from builtins import input


user=int(input("no"))
i=1
c=0
while i<=user:
    if user%i==0:
        c=c+1
    i=i+1
if c==2:
    print("prime no")
else:
    print("no")