#Indicate whether between two numbers if both are even or which one is even.
def even_or_odd(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("The numbers are even")
    elif num1 % 2 == 0 and num2 % 2!= 0:
        print("The first number is even")
    elif num1 % 2!= 0 and num2 % 2 == 0:
        print("The second number is even")
    else:
        print("The numbers are odd")

even_or_odd(num1=int(input("Enter the first number: ")), num2=int(input("Enter the second number: ")))
