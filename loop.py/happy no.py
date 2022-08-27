from builtins import input


n=int(input("no"))
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+(r**2)
        x=x//10
    x=sum
if x==1:
    print("happy no")
else:
    print("no")   
    