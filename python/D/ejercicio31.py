#Calculate the salary of an employee according to his category:
#The category A = 10%
#The category B = 15%
#The category C = 23%
#The category D = 25%

def salary(Category, Number_hours, Value_hours):
    Value_total= Number_hours*Value_hours

    if Category == 'A':
        Salary_Incremet = Value_total*0.1
        print(f"For category A, increase of 10% of their total hourly wage then their wage will be: {Salary_Incremet}")
    elif Category == 'B':
        Salary_Incremet = Value_total*0.15
        print(f"For category B, increase of 15% of their total hourly wage then their wage will be: {Salary_Incremet}")
    elif Category == 'C':
        Salary_Incremet = Value_total*0.23
        print(f"For category C, increase of 23% of their total hours wage then their wage will be: {Salary_Incremet}")
    elif Category == 'D':
        Salary_Incremet = Value_total*0.25
        print(f"For category D, increase of 25% of their total hours wage then their wage will be: {Salary_Incremet}")
    else:
        print("Invalid Category does not incremen of the salary")

salary(Category=input("Selection one Category.(A,B,C,D): "),Number_hours=int(input("Number of the hours jobs: ")),Value_hours=int(input("Value of the hours jobs: ")))
