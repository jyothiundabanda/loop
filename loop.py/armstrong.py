# n=int(input("enter"))
# a=n
# s=0
# while n>0:
#     s=s+(n%10)*(n%10)*(n%10)
#     n=n//10
# if a==s:
#     print("pri")
# else:
#     print("n")

from builtins import input


n=int(input("n0"))
a=n
s=0
len=len(str(n))
while n>0:
    r=n%10
    b=r**len
    s=s+b
    n=n//10
if s==a:
    print("amstrong number")
else:
    print("not")
   