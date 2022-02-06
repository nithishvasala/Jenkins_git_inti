# Factorial

def factorial(num):
    if (num<0):
        return 0
    elif(num==0 or num==1):
        return 1
    else:
        fact =1
        while(num>1):
            fact=num*fact
            num=num-1
        return fact
            
x=factorial(6)
print(x)
        
