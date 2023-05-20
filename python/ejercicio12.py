#Given two numbers calculate the larger one.

number_one= int(input("Enter a number: "))
number_two= int(input("Enter a number: "))

if number_one>number_two:
    print(f"The first number ({number_one}) is more that the second number ({number_two})")
elif number_two>number_one:
    print(f"The second number ({number_two}) is more that the first number ({number_one})")
else:
    print("All numbers are some")