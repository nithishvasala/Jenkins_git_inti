# amstrong number


num = int(input("enter a number"))
sum=0
temp = num
while(temp>0):
    x = temp%10
    y = x**3
    temp = temp//10
        
if num == x:
    print("amstrong")
else:
    print("not amstrong")
