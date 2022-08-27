from builtins import input


amount=int(input("enter the amount"))
note2000=note500=note100=note50=note20=note10=0
if amount>=2000:
    note2000=amount//2000
    print("no of 2000 notes amount:",note2000)
if amount>=500:
    note500=amount//500
    print("no of 500 notes amount:",note500)
if amount>=100:
    note100=amount//100
    print("no of 100 notes amount:",note100)
if amount>=50:
    note50=amount//50
    print("no of 50 notes amount:",note50)
if amount>=20:
    note20=amount//20
    print("no of 20 notes amount:",note20)
if amount>=10:
    note10=amount//10
    print("no of 10 notes amount:",note10)
else:
    print("nothing")
