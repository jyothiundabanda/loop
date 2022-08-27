from builtins import input


# n=int(input("no"))
# a=n
# sum=0
# while n>0:
#     r=n%10
#     sum=sum+r
#     n=n//10
# if a%sum==0:
#     print("harshed no")
# else:
#     print("not")

n=int(input("no"))
r=str(n)
i=0
s=0
while i<len(r):
    a=n%10
    m=a*a
    n=n//10
    i=i+1
    s=s+m
    print(m)
print(s)

# n=int(input("no"))
# i=1
# while i<=n:
#     if i%2!=0 and i%3!=0:
#         print(i)
    
#     i=i+1


# n=int(input("no"))
# i=1
# while i<=n:
#     if i%2!=0 and  i%11==0:
#         print(i)
    
#         # print(i)
#     i=i+1