user=int(input("no"))
i=0
min=user
max=0
while i<user:
    user1=int(input("no"))
    if user1<min:
        min=user1
    elif user1>max:
        max=user1
    i+=1
print(min)
print(max)

# i=0
# min=100
# max=0
# user=int(input("no"))
# while i<user:
#     user1=int(input("no"))
#     if user1>max:
#         max=user1
#     elif user1<min:
#         min=user1
#     i+=1
# print(min,"is min")
# print(max,"is max")

from fileinput import input

# n=int(input("no"))
# i=0
# max=0
# min=n
# user=int(input("no"))
# while i<user:
#     user1=int(input("no"))
#     if user1>max:
#         user1=min
#     elif user<=min:
#         user1=max
#     i=i+1
# print(max)
# print(min)