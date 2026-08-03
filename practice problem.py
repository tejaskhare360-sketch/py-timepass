
#Variables & Data Types | Lecture 1
#first
num1 = int(input(" Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
print("The sum of" , num1, "and" , num2 , "is" , sum)

#second (area finding of a square) 

side= int(input("enter the side of a squre"))
area = side*side
print("the area of the square is", area) 

side2 = float(input("Enter the side of the square: "))
area2 = side2*side2
print("The area of the square is:", area2)

#third (average of 2 floating numbers) 

float1 = float(input("Enter the first floating number: "))
float2 = float(input("Enter the second floating number: "))
average = (float1 + float2)/2

print("average : " , average)

#fourth (true or false question)

a = int(input(" enter a number: "))
b = int(input("enter another number: "))

print( a >= b)