#Design an algorithm that shows if a person has income or not, it must indicate the income and indicate income and expenses, the balance must be validated.

income= float(input("enter your income: "))
expenses= float(input("enter your expenses: "))
balance= income-expenses

if balance <0:
    print("Your financial status is in the red.")
elif balance <2000:
    print("Your financial situation is moderately bad and you should make an effort to work harder.")
elif balance <3000:
    print("Your financial situation is regularly well.")
else:
    print("Your financial status is very good.")
