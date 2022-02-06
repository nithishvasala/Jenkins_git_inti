# check prime number

num = int(input("enter number"))
if num<2:
    print("not a prime number")
else:
    for x in range(2,num):
        if num%x ==0:
            print("not a prime number")
            break
    else:
        print("prine numer")
