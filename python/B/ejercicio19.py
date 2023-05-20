

number_one= int(input("Enter a number: "))
number_two= int(input("Enter a number: "))
number_three= int(input("Enter a number: "))

if number_one>number_two and number_three:
    print(f"The first number ({number_one}) is greater that the second number ({number_two})and the third number ({number_three}).")
elif number_two>number_one and number_three:
    print(f"The second number ({number_two}) is greater that the fist number ({number_one}) and third number ({number_three}).")
elif number_three>number_one and number_two:
    print(f"The third number ({number_three}) is greater that the first number ({number_one}) and second number ({number_two}).")
else:
    print("All numbers are some.")
