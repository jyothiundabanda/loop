from builtins import input


year=int(input("enter the number"))
month=int(input("enter the month"))
day=int(input("enter the day"))
if day>=1 and day<=31 or month>=1 and month<=12 or year>1 and year<=20000:
    print(year+1,"/",month+1,"/",day+1)
else:
    print("ntg")
    