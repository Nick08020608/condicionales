#Design an algorithm that captures two numbers, and performs the sum of those numbers, and display the data if the result is not negative.

number= int(input("Ienter a number: "))
number_two= int(input("enter a number: "))
 
sum= number+number_two

if sum >0:
    print("The value of the sum is: ", sum)
else:
    print("Because it is a negative number I cannot perform the operation....")
