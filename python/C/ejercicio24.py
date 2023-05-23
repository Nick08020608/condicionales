#Develop a program that checks whether a year is a leap year.

def main():
    year = int(input("Enter a year: "))
    if year % 4 == 0 and year % 100!= 0 or year % 400 == 0:
        print(f"{year} is an even year.")
    else:
        print("this year is not even.")

main(year=int(input("Enter a year: ")))