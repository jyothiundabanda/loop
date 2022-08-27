# num=int(input("enter the number"))
# if num>="a" and num<="z" or num>="A" and num<="Z":
#     print(num,"is a alphabets")
# elif num>="0" and num<="9":
#     print(num,"is a digits")
# else:
#     print("it is aspecial character")


name=input("name")
age=int(input("enter the no"))
gender=input("enter the name")
if age>=18:
	if gender=="male":
		print("hello",name,"wellcome")
	else:
		print("hello mis",name,"wellcome")
else:
	print("you are not eligible")