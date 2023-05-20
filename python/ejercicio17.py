#Make a program that asks for two numbers and prints them in ascending and descending order.

number_one= int(input("Enter a number: "))
number_two= int(input("Enter a number: "))

if number_one <= number_two:
    print(f"The order of the numbers {number_one} and {number_two} would be placed in ascending order and would end as follows:\n{number_one,number_two:}")
else:
    print(f"The orden of the numbers {number_one} and {number_two} would be placed in descending order and would end as follows:\n{number_two,number_one}")
