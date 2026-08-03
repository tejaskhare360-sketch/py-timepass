#wap to check weather the number is odd or even 

num = int(input("enter a number:"))
if num % 2 == 0:
    print(num, "is an even number")
else: 
    print(num, "is an odd number")

#wap to find the greatest 3 numbers entered by the user

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:")) 

if num1 > num2 and num1 > num3:
    print(num1, "is the greatest number")
elif num2 > num1 and num2 > num3: 
    print(num2, "is the greatest number")
else: 
    print(num3, "is the greatest number")

#program to check the num is multiple of 7 or not. 

x = int(input("enter a number:"))
if x % 7 == 0:
    print(x, "is a multiple of 7")
else:
    print(x, "is not a multiple of 7")

