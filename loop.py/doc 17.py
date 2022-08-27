n=int(input("no"))
i=n
s=0
while n>0:
    s=s+(n%10)*(n%10)*(n%10)
    n=n//10
if i==s:
    print("amsrong no")
else:
    print("not")

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