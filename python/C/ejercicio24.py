#Develop a program that checks whether a year is a leap year.

def main(year):
    
    if year % 100!= 0 and year % 400 == 0:
        print(f"{year} is an even year.")
    else:
        print("this year is not even.")

main(year=int(input("Enter a year: ")))