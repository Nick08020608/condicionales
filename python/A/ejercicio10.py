#Display the sum of two integers, if the result exceeds 10.

number_one= int(input("Enter number: "))
number_two= int(input("Enter number: "))

sum= number_one+number_two

if sum >10:
    print(f"The result is {sum:.0f}")
