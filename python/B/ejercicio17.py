#Make a program that asks for two numbers and prints them in ascending and descending order.

list=[]
number_one= int(input("Enter a number: "))
number_two= int(input("Enter a number: "))

list.append(number_one)
list.append(number_two)

print(f"\n ")

list.sort()

print(f"list in ascending order: {list}")

list.reverse()

print(f"list in a decent way: {list}")
