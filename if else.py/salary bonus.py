from builtins import input


salary=int(input("enter the salary"))
year=int(input("enter the year"))
bonus=salary*5/100
if year>=5:
    print(bonus,"is net bonus")
else:
    print('no net bonus')



    salary=int(input("enter the salary"))
    if salary<=10000:
        hra=20%0
        da=80%0
        print(salary+hra+da,"is gross salary")
    elif salary<=20000:
        hra=25
        da=90
        print(salary+hra+da,"is gross salary")
    elif salary>=20000:
        hra=30
        da=95
        print( salary+hra+da,"is gross salary")