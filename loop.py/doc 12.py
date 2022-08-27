n=int(input("no"))
i=1
while i<=n:
    i=i*(n%10)
    n=n//10
print(i)