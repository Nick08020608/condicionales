#Make a program that asks for 3 numbers and indicates whether the third is equal to the sum of the first and the second.

number_one= int(input("Enter a number: "))
number_two= int(input("Enter a number: "))
number_three= int(input("Enter a number: "))
sum=number_one+number_two

if sum == number_three:
    print(f"The sum on the first number {number_one} and the second number {number_two} result in {number_three}")
else:
    print(f"the sum does not result in {number_three} but results in: {sum}")