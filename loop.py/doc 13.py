from builtins import input


i=0
n=int(input("no"))
while n>0:
    i=i*10+(n%10)
    n=n//10
print(i)