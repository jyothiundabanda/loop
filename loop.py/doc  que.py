# i=0
# n=int(input("enter "))
# while i<=n:
#     print(i)
#     i=i+2


# i=1
# user=int(input("enter the no"))
# while i<=user:
#     print(i)
#     i=i+1

# i=1
# user=int(input("enter the no"))
# while i<=user:
#     print(i,i*i)
#     i=i+1
# i=10
# user=int(input("no"))
# while i<=user:
#     print(i)
#     i+=10

# i=0
# user=int(input("no"))
# while user>0:
#     i=i*10+user%10
#     user=user//10
# print(i)


# i=1
# s=0
# while i<10:
#     user=int(input("enter the no"))
#     s=s+user
#     i+=1
# print(s)


# i=1
# s=0
# user=int(input("no"))
# while i<=user:
#     if i%2==0:
#         s=s+i
#     i=i+1
# print(s)

# i=1
# user=int(input("no"))
# while i<user:
#     print(i,i*i)
#     i=i+1

# i=1
# s=0
# while i<=10:
#     # user=int(input("enter the no"))
#     s=s+i
#     i+=1
# print(s)

n=int(input("no"))
i=1
while n>0:
    i=i*n%10
    n=n//10
print(i)