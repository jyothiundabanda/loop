
# for i in range (1,10):
#     print(i)
# for i in range (5):
#     print(i)

# for i in (1,2,3):
#     print(i)

# for i in (2,3,4):
#     print("i")

# for i in (4,3,2,1,0):
#     print(i,end="")

# for i in range (10):
#     if i%2!=0:
#         print("hello",i)

# for i in range (10,2,-2):
#     print(i)

# str="python output based questions"
# word=str.split()
# for i in word:
#     print(i)

# for i in range (7,10):
#     print("python output based questions")
#     print("python output based questions")

# for i in range (7,-2,-9):
#     for j in range(i):
#         print(i)

# i="9"
# for k in i:
#     print(k)

# for i in range (1,8):
# #     print(i)
#     i=i+2
#     print(i)

# for i in range(4,7):
#     i=i+3
#     print("hello",i)

# for i in range(20):
#     if i//4==0:
#         print(i)

# x=1234
# while x%10:
#     x=x//10
#     print(x)

# [17]:
# for i in 1,2,3:
#     print(i*i)

# [18]:
# for i in 2,4,6:
#     print("H"*i)

# [19]:
# p=10
# q=20
# p=p*q//4
# q=p+q**3
# print(p,q)

# [20]:
# x=2
# y=6
# x=x+y/2 + y//4
# print(x)

# [21]:
# n=11
# for i in range(2,n//2):
#     if n%i!=0:
#         print("Python Output based Questions")
#         break
#     else:
#         print("Bye")
from builtins import input


# n=int(input("no"))
# for i in range(1,n-1):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

for i in range(6):
    for j in range(7):
        if i==0 and j%3!=0 or i==1 and j%3==0 or i-j==2 or i+j==8:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()