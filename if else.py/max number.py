from builtins import input


a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
	print(a,"is a maximun")
elif b>a and b>c:
	print(b,"is a maximum")
elif c>a and c>b:
	print(c," is a maximum")
else:
	print("ntg")