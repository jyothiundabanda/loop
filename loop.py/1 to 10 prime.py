i=1
while i<=10:
    j=2
    count=0
    while j<i:
        if i%j==0:
            count=count+1
        j+=1
    if count==0:
        print(i,"prime number")
    i+=1



    