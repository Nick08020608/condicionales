#Design an algorithm that, when entering the user's age, if he/she is of legal age, displays a message "he/she is of legal age".

age = int(input("Enter your age: "))

if age >=18:
    print("You are of legal age")
else:
    print("You are a minor")
