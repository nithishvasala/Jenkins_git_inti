# Palindrome number

def palindrome(num):
    x=num[::-1]
    if x == num:
        print ("Palindrome")
    else:
        print ("Not Palindrome")
        

print(palindrome("12321"))
