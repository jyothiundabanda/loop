# i=156
# j=157
# while i<246:
#     if j-i==11:
#         break
#     else:
#         print(j-i)
#     j+=1

# prime or not

from builtins import input
i=1
count=0
num=int(input("enter the number"))
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime number")
else:
    print("not")